#!/bin/sh
#
#   http://code.google.com/media-translate/
#   Copyright (C) 2010  Serge A. Timchenko
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#

DAT_FILE=/tmp/xspf_renderer.dat
STATUS_FILE=/tmp/xspf_renderer.status

urldecode()
{
  awk '
  BEGIN{
  	for(i = 0; i < 10; i++)
  		hex[i] = i
  	hex["A"] = hex["a"] = 10
  	hex["B"] = hex["b"] = 11
  	hex["C"] = hex["c"] = 12
  	hex["D"] = hex["d"] = 13
  	hex["E"] = hex["e"] = 14
  	hex["F"] = hex["f"] = 15
  }
  {
  	gsub(/\+/, " ")
  	i = $0
  	while(match(i, /%../)){
  		if(RSTART > 1)
  			printf "%s", substr(i, 1, RSTART-1)
  		printf "%c", hex[substr(i, RSTART+1, 1)] * 16 + hex[substr(i, RSTART+2, 1)]
  		i = substr(i, RSTART+RLENGTH)
  	}
  	print i
  }
  '
}

if [ "$QUERY_STRING" = "renderer=stop" -o "$QUERY_STRING" = "renderer=pause" -o "$QUERY_STRING" = "renderer=play" ]; then
  echo ${QUERY_STRING} | sed 's/=/-/;s/.*/{\0}/' > $DAT_FILE
  sleep 5
elif echo "$QUERY_STRING" | grep -qs "url="; then
  echo ${QUERY_STRING} | sed 's/.*url=//' | urldecode > $DAT_FILE
  sleep 5
fi

RENDERER_STATUS='not running'
RENDERER_URL=''

if [ -f $STATUS_FILE ]; then
  RENDERER_STATUS=`sed -n '1p' $STATUS_FILE`
  RENDERER_URL=`sed -n '2p' $STATUS_FILE`
  #rm -f $STATUS_FILE
fi

if [ -n "$QUERY_STRING" ]; then
  echo "Content-type: text/plain"
  echo ""
  echo "(function(){ return { status:\"$RENDERER_STATUS\", url:\"$RENDERER_URL\"}; })();"
else

cat <<EOF
Content-type: text/html

<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="Pragma" content="no-cache">
<title>Media Stream Renderer - Control</title>
<style>
  .btn { width:60px; }
</style>
<script type="text/javascript" language="javascript">
  var makeRequest = function(para) {
    var http_request = false;
    if (window.XMLHttpRequest) { // Mozilla, Safari, ...
      http_request = new XMLHttpRequest();
      if (http_request.overrideMimeType) {
              http_request.overrideMimeType('text/plain');
      }
    } else if (window.ActiveXObject) { // IE
      try {
        http_request = new ActiveXObject("Msxml2.XMLHTTP");
      } catch (e) {
        try {
          http_request = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {}
      }
    }
    if (!http_request) {
      alert('errorXMLHTTP');
      return null;
    }
    var url = "$SCRIPT_NAME" + para;
    http_request.onreadystatechange = function() { updateContents(http_request); };
    http_request.open('get', url, true);
    http_request.setRequestHeader("If-Modified-Since", "Thu, 1 Jan 1970 00:00:00 GMT");
    http_request.setRequestHeader("Cache-Control", "no-cache");    
    http_request.send(null);
  }
  function updateContents(http_request) {
    if (http_request.readyState == 4) {
      if (http_request.status == 200) {
        var data = eval(http_request.responseText);
        document.getElementById('status').innerHTML = data.status;
        document.getElementById('url').value = data.url;
      } 
      //else { alert('request trouble'); }
    }
  }
  window.onload = function() {
    setInterval(function(){makeRequest("?refresh")}, 5000);
  }
</script>
</head>
<body>
EOF
echo "<table border=0 cellpadding=10>"
echo "<tr><td colspan=2><table border=0 width=100%><td><h1><a href=\"$SCRIPT_NAME\">Media Stream Renderer</h1></a></td><td align=right><img src=/img/msr_w.png></td></tr></table><hr></td></tr>"
echo "<tr><td>Status:</td><td><span id=status>$RENDERER_STATUS</span></td></tr>"
echo "<tr><td>Stream URL:</td><td><form action=\"$SCRIPT_NAME\" method=get><input id=url type=text name=url value=\"$RENDERER_URL\" size=64><input class=btn type=button value=Submit onclick='makeRequest(\"?url=\"+encodeURIComponent(document.getElementById(\"url\").value))'></form></td></tr>"

echo "<tr><td>Renderer control:</td>"
echo "<td><form action=\"$SCRIPT_NAME\" method=get><input class=btn type=button name=renderer value=stop onclick='makeRequest(\"?renderer=stop\")'></form>"
echo "<form action=\"$SCRIPT_NAME\" method=get><input class=btn type=button name=renderer value=pause onclick='makeRequest(\"?renderer=pause\")'></form>"
echo "<form action=\"$SCRIPT_NAME\" method=get><input class=btn type=button name=renderer value=play onclick='makeRequest(\"?renderer=play\")'></form></td>"
echo "</tr>"
echo "<tr><td colspan=2 align=center><hr></td></tr>"
echo "</table>"
echo "<h3>Internet browser extensions</h3><ul>"
echo "<li><a href="/bin/playonplayer.xpi">Firefox</a></li>"
echo "<li><a href="/bin/playonplayer.exe">Internet Explorer</a></li>"
echo "<li><a href="/bin/playonplayer.crx">Google Chrome</a></li>"
echo "</ul>"

echo "</body>"
echo "</html>"

fi