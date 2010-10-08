/*
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
*/

chrome.extension.onRequest.addListener(
  function(request, sender, sendResponse) {
    var w = window;
    if(request.status)
    {
      alert(request.status);
      w.status = request.status;
    }
    else
    {
      var streamUrl = '';
      if(w.document.selection)
      {
        var sel = w.document.selection;
        if(sel.type.toLowerCase() == 'text')
        {
          streamUrl = sel.createRange().text.replace(/(^\s+|\s+$)/, '');
        }
      }
      
      if(!streamUrl)
      {
        var active = w.document.activeElement;
        while(active && active.tagName.toLowerCase() != 'a' && active.tagName.toLowerCase() != 'body' )
          active = active.parentNode;
        if(!active || active.tagName.toLowerCase() == 'body')
          streamUrl = w.document.URL;
        else
          streamUrl = active.href;
      }
      sendResponse({"href": streamUrl});
    }
});
