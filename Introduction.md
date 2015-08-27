# Назначение #

Пакет представляет собой набор RSS/CGI-приложений и плейлистов, которые дополняют/расширяют функциональность стандартных интернет сервисов в плеерах построенных на чипсетах Realtek 1073/1283.

# Интегрированные online-сервисы и плейлисты #

> ## Internet Video ##
> ### Сервисы ###
  * Youtube (http://youtube.com)
  * Rutube (http://rutube.ru)
  * IVI Music (http://music.ivi.ru)
  * Zoomby Music (http://www.zoomby.ru/music)
  * Мосфильм (http://cinema.mosfilm.ru)
  * URAVO.TV (http://uravo.tv/)
  * 24video.net (http://www.24video.net/)
> ### RSS-ленты и плейлисты ###
  * Sovok TV (http://sovok.tv)
  * Tvigle (http://tvigle.ru)
  * IVI (http://ivi.ru)
  * Vimeo (http://vimeo.com)
  * OneHD (http://live.1hd.ro)
  * Мультики (http://mults.spb.ru)
  * Rutube трансляции (http://rutube.ru/channels.html)
  * Kiwi.kz (http://kiwi.kz)
  * HD Kinomir (http://hdkinomir.com)
  * Filmix.net (http://filmix.net)
  * AniMult.tv (http://animult.tv)
  * Kino-Dom.tv (http://kino-dom.tv)
  * LineCinema.ru (http://www.linecinema.org)
  * Rock Television (http://rocktelevision.com)

> ## Internet Radio ##
> ### Сервисы ###
  * SHOUTcast Directory (http://shoutcast.com)
  * RadioTime (http://radiotime.com/)
  * Poiskm.ru (http://poiskm.ru/)
> ### Интернет радиостанции ###
  * SomaFM (http://somafm.com/)
  * Digitally Imported (http://di.fm/)
  * SKY.fm (http://sky.fm/)
  * JAZZRADIO (http://www.jazzradio.com/)
  * 1.FM (http://1.fm/)
  * 181.FM (http://181.fm/)
  * Radioio (http://radioio.com/)
  * Bluemars (http://www.bluemars.org/)
  * RauteMusik (http://rautemusik.fm/)
  * Station.ru (http://station.ru/StationsList.aspx?type=online)
  * Nullwave.ru (http://nullwave.ru/)
  * Sampo.ru (http://radio.sampo.ru/)
  * BBC Radio (http://http://www.bbc.co.uk/radio/)
  * CBC Radio (http://www.cbc.ca/radio/)

# Встроенные RSS/CGI-приложения #
> ## Media Stream Renderer ##

> Проигрывание медиа ссылок на плеере с локального компьютера.

> ## XSPF Browser ##

> Браузер списков воспроизведения и проигрыватель медиаконтента с локальных дисков, http- и ftp-серверов.

# Поддерживаемый контент #

Сетевые протоколы:
  * HTTP, FTP, MMS, MMSH, RTSP (используется [msdl](http://msdl.sourceforge.net/));
  * RTMP, RTMPE (используется [flvstreamer](http://flvstreamer.sourcearchive.com/));
  * UDP, RTP (через [udpxy](http://sourceforge.net/projects/udpxy/));
  * ICY - получение информации о текущем проигрываемом треке.

Помимо прямых ссылок на аудио/видео потоки и плейлисты, с помощью плагинов возможно получение и проигрывание медиапотоков по косвенным ссылкам от ряда контент провайдеров, список которых приведен ниже. Использование плагинов позволяет достаточно просто расширять данный список.

Поддерживаемые контент провайдеры с примерами ссылок:
  * [Youtube](http://www.youtube.com/)
```
http://www.youtube.com/v/JZtcw6GIxTY
http://www.youtube.com/watch?v=JZtcw6GIxTY
```
  * [Vimeo](http://vimeo.com/)
```
http://vimeo.com/13768695
http://vimeo.com/moogaloop.swf?clip_id=13199616
http://vimeo.com/channels/timelapseinhd/videos/rss
```
  * [SHOUTcast](http://www.shoutcast.com/)
```
http://yp.shoutcast.com/sbin/tunein-station.pls?id=1116397
```
  * [RadioTime](http://radiotime.com/)
```
http://opml.radiotime.com/Tune.ashx?id=s29667&sid=p30125
```
  * [IVI](http://ivi.ru/) (_Замечание._ Требуется наличие **[curl](http://code.google.com/p/media-translate/wiki/Installation#%D0%92%D1%81%D0%BF%D0%BE%D0%BC%D0%BE%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D1%83%D1%82%D0%B8%D0%BB%D0%B8%D1%82%D1%8B)**.)
```
http://www.ivi.ru/video/view/?id=2756
http://france.ivi.ru/movie.php?id=2490
```
  * [Tvigle](http://tvigle.ru/)
```
http://www.tvigle.ru/category/cinema/1882?video=483307
```
  * [Трансляции Rutube.ru](http://rutube.ru/channels.html)
```
http://rutube.ru/tv/o2tv.html
```
  * [RuTube](http://rutube.ru/)
```
http://rutube.ru/tracks/1088305.html?v=1c21315933044e39fdd57808ac5e3958
http://video.rutube.ru/1c21315933044e39fdd57808ac5e3958
```
  * [Интернет радиостанции Station.ru](http://station.ru/StationsList.aspx?type=online)
```
http://station.ru/RadioStation.aspx?id=1743
```
  * [Медиа-каталог Игоря Гузей](http://guzei.com/)
```
http://guzei.com/online_radio/listen.php?online_radio_id=5325
http://guzei.com/online_tv/watch.php?online_tv_id=1781
```
  * [Радио-каталог Radiogrom.com](http://www.radiogrom.com/online/)
```
http://www.radiogrom.com/online/russia/radio_priboy_online.html
http://www.radiogrom.com/online/belarus_fm/evroradio_online.html
```
  * [live-online-tv.com](http://www.live-online-tv.com/)
```
http://www.live-online-tv.com/tv/planeteinsolite.html
```
  * [mults.spb.ru](http://mults.spb.ru/)
```
http://mults.spb.ru/mults/?id=696
```
  * [Zoomby](http://www.zoomby.ru/)
```
http://www.zoomby.ru/watch/4396-kamenskaya-3
```
  * [Золотая коллекция киностудии Мосфильм](http://cinema.mosfilm.ru/)
```
http://www.cinema.mosfilm.ru/Film.aspx?id=ee914026-6828-4327-9f31-a3a63623dbd1
```
  * [filmix.net](http://filmix.net/)
```
http://filmix.net/anime/15038-golos-dalekoy-zvezdy-hoshi-no-koe-2003.html
```
  * [linecinema.org](http://linecinema.org/), [kino-dom.tv](http://kino-dom.tv/), [filin.tv](http://filin.tv/), [animult.tv](http://animult.tv/)
```
http://www.linecinema.org/newsz/komedyya-online/504343-ya-vse-esche-zdes-poteryannyy-god-hoakina-feniksa-2010eng.html
http://kino-dom.tv/comedi/735-yepizody-episodes-1-sezon-1-seriya-onlajn.html
http://www.filin.tv/otechestvennue/561-marusya-smotret-onlajn.html
http://animult.tv/anime/animeser/725-magicheskij-indeks-to-aru-majutsu-no-index-1-24-serii-iz-24-onlajn.html
```
  * [zaycev.net](http://zaycev.net/)
```
http://zaycev.net/pages/8628/862805.shtml
```
  * [Rock Television - Cult & Rare](http://cultandrare.rocktelevision.com/)
```
http://cultandrare.rocktelevision.com/Player/TabId/58/VideoId/233/DIRE-STRAITS-Sultans-Of-Swing.aspx
```
  * [YouRock by Rocktelevision](http://yourock.rocktelevision.com/)
```
http://yourock.rocktelevision.com/VideoPlayer/TabId/56/VideoId/508/ORANGE-LEM--Geometric-Woman.aspx
```
  * [ВКонтакте](http://vk.com/)
```
http://vk.com/video_ext.php?oid=92898632&id=160253092&hash=37757274d849df4a&hd=1
http://vkontakte.ru/video_ext.php?oid=8386018&id=158808447&hash=50976b98544a296c&hd=1
```
  * [HD Киномир](http://hdkinomir.com/)
```
http://hdkinomir.com/comedy/1465-madagaskar-madagascar-2005-onlayn.html
```
  * [24video.net](http://24video.net/)
```
http://www.24video.net/video/view/1229075?feature=indexfreshfilter2
```
  * [Совок ТВ](http://sovok.tv/)
```
http://sovok.tv/api.php?channel=33
```
  * [Интернет-кинотеатр URAVO.TV](http://uravo.tv/)
```
http://www.uravo.tv/cartoon/389/
http://www.uravo.tv/documentary/656/
http://www.uravo.tv/movie/215/
```
  * [Videomore](http://videomore.ru/)
```
http://videomore.ru/tracks/inostrannaia_kuhnia/40-seriya?auto=true
```
  * [tvzavr.ru](http://www.tvzavr.ru/)
```
http://www.tvzavr.ru/online-kino/5060
```
  * [MY-HIT.RU](http://www.my-hit.ru/)
```
http://my-hit.ru/film/8330/online
http://my-hit.org/film/8330/online
```
  * [Last.FM](http://www.last.fm/api)
> Получение изображения с исполнителем для текущего проигрываемого трека.