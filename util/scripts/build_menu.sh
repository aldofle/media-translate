#!/bin/sh
#
# menu generator
#

BASEPATH=/usr/local/etc/translate
TRANSLATE_CGI=`sed -n '1p' $BASEPATH/etc/cgi.conf`

if [ -z "$1" -o -z "$2" ]; then
  echo "Usage: $0 <link_url> <rss_file_name>"
  exit 0;
fi

wget -q -O  - $1 | awk -v basepath="$BASEPATH" -v translate_cgi="$TRANSLATE_CGI" '
  {
    if(match($0, /<link>(.*)<\/link>/, arr))
    {
      url=arr[1];
      if(match(url, /.*,(collection|moskvafm)\//))
      {
        file="";
        if(match(url, /File:([^,;]*)[,;]/, arr))
        {
          file=arr[1];
        }
        else if(match(url, /app,([^,;]*)[,;]/, arr))
        {
          file=arr[1];
        }
        file_rss=file;
        gsub(/\//, "-",file_rss);
        sub(/\.xspf/, ".rss", file_rss);
        print "<link>rss_file://../etc/translate/rss/" file_rss "</link>";
        cmd=basepath "/util/scripts/build_menu.sh \"" url "\" \"" basepath "/rss/" file_rss "\"";
        print file_rss > "/dev/stderr" 
        system(cmd);
      }
      else if(url ~ translate_cgi)
      {
        print "<link><script>translate_base_url+\"" substr(url, length(translate_cgi)+1) "\";</script></link>"
      }
      else
        print;
    }
    else
      print;
  }
' > $2



