#!/bin/sh
#
# menu generator
#

BASEPATH=/usr/local/etc/translate

if [ -z "$1" -o -z "$2" ]; then
  echo "Usage: $0 <link_url> <rss_file_name>"
  exit 0;
fi

wget -q -O  - $1 | awk -v basepath="$BASEPATH" '
  {
    if(match($0, /<link>.*,(collection|moskvafm)\//))
    {
      match($0, /<link>(.*)<\/link>/, arr);
      url=arr[1];
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
      print "<link>rss/" file_rss "</link>";
      cmd=basepath "/util/scripts/build_menu.sh \"" url "\" \"" basepath "/rss/" file_rss "\"";
      print file_rss > "/dev/stderr" 
      system(cmd);
    }
    else
      print;
  }
' > $2



