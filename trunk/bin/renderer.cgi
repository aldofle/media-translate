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
  li { padding-top:5px; }
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
        var textElement = document.getElementById('url');
        if(document.activeElement != textElement)
    	    textElement.value = data.url;
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
echo "<h3>Internet browser extensions <a href="http://code.google.com/p/media-translate/wiki/ModuleMediaStreamRenderer#Add-on_%D0%B4%D0%BB%D1%8F_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82_%D0%B1%D1%80%D0%B0%D1%83%D0%B7%D0%B5%D1%80%D0%BE%D0%B2"><sup>[?]</sup></a></h3>"
echo "<ul>"
echo "<li><a href="/bin/playonplayer.xpi">Firefox</a></li>"
echo "<li><a href="/bin/playonplayer.exe">Internet Explorer</a></li>"
echo "<li><a href="/bin/playonplayer.crx">Google Chrome</a></li>"
echo "<br><li>Opera Custom Buttons: "
echo "<a id="operafindandplay" style=\"border:1px grey solid; background-color:lightgrey; color:black; padding:0px 5px 0px 5px ; text-decoration:none !important; \" href=\"\">Find and Play</a>"
echo "<a id="operaplayonplayer" style=\"border:1px grey solid; background-color:lightgrey; color:black; padding:0px 5px 0px 5px ; text-decoration:none !important; \" href=\"\">Play on Player</a>"
echo "<span style=\"margin-left:10px; \"><label>Player IP or name: <label><input type=\"text\" id=\"playertext\" size=\"20\" value=\"player\"><button onclick=\"refreshOperaButtons()\">Ok</button></span>"
echo "<ul>"
echo "<script language=\"javascript\">"
cat <<EOF
function refreshOperaButtons() 
{ 
  var player = playertext.value;
  var syntax = "opera:/button/Go to page, \"javascript: var stp = function() { var mr = function(url) { var hr = false; if (window.XMLHttpRequest) { hr = new XMLHttpRequest(); if (hr.overrideMimeType) { hr.overrideMimeType('text/xml'); } } if (!hr) alert('errorXMLHTTP'); hr.open('get', url, false); hr.setRequestHeader('If-Modified-Since', 'Thu, 1 Jan 1970 00:00:00 GMT'); hr.setRequestHeader('Cache-Control', 'no-cache'); hr.send(); return hr.status; }; return { run : function(s) { var p = '"+player+"'; try { var u = 'http://'+p+'/cgi-bin/translate?renderer,,' + encodeURIComponent(s); var r = mr(u); window.status = 'Link <'+s+'> sent to player <'+p+'> ('+r+')'; } catch(e) { alert('ERROR: '+e.description); } } }; }(); var b=new Array(); var c=1; var o=((document.onkeydown==null)||(o==2))?0:1; document.onkeydown=ck; z=document.getElementsByTagName('A'); for(i=0;i<z.length;i++) { z[i].onclick=function(e){t=this;if(window.event) e=window.event;if((t==e.target)||(window.event)) { stp.run(t.href); } if(window.opera) e.stopPropagation();return false;}; z[i].onmouseover=function(){if(!c)return;c=0;t=this;b[t]=t.style.backgroundColor;t.style.background='#FF9999';}; void(z[i].onmouseout=function(){t=this;t.style.backgroundColor=b[t];c=1;}); } function ck(e) { k=window.event?window.event.keyCode:e.keyCode; if((k==27)||o) { o=2; document.onkeydown=null; for(i=0;i<z.length;i++) { z[i].onclick=null; z[i].onmouseover=null; z[i].onmouseout=null; z[i].style.backgroundColor=b[t]; } } } if(o==1) ck(1); \",1,,\"Play on Player\"";
  document.getElementById('operafindandplay').href = syntax;
  var syntax = "opera:/button/Go to page, \"javascript: var stp = function() { var mr = function(url) { var hr = false; if (window.XMLHttpRequest) { hr = new XMLHttpRequest(); if (hr.overrideMimeType) { hr.overrideMimeType('text/xml'); } } if (!hr) alert('errorXMLHTTP'); hr.open('get', url, false); hr.setRequestHeader('If-Modified-Since', 'Thu, 1 Jan 1970 00:00:00 GMT'); hr.setRequestHeader('Cache-Control', 'no-cache'); hr.send(); return hr.status; }; return { run : function(s) { var p = '"+player+"'; try { var u = 'http://'+p+'/cgi-bin/translate?renderer,,' + encodeURIComponent(s); var r = mr(u); window.status = 'Link <'+s+'> sent to player <'+p+'> ('+r+')'; } catch(e) { alert('ERROR: '+e.description); } } }; }(); stp.run(document.URL);\",1,,\"Play on Player\"";
  document.getElementById('operaplayonplayer').href = syntax;
}
refreshOperaButtons();
EOF
echo "</script>"
echo "</ul>"

echo "</body>"
echo "</html>"

fi