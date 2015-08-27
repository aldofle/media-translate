# Установка #

  * Пакет устанавливается в директорию **/usr/local/etc/translate**:
```
mkdir -p /usr/local/etc/translate
cd /usr/local/etc/translate
```

> _Или_, если объем доступного места в **/usr/local/etc** на плеере не позволяет этого сделать, то можно создать символическую ссылку с именем **/usr/local/etc/translate** на реальное расположение файлов (например, если /home это ext3 раздел диска):
```
mkdir -p /home/translate
cd /home/translate
ln -s /home/translate /usr/local/etc/translate 
```

  * Загружаем и распаковываем текущую версию пакета:
```
wget -O /tmp/mt.tar.bz2 http://media-translate.googlecode.com/files/rss_ex_2.0.10.tar.bz2
tar -xjf /tmp/mt.tar.bz2
rm /tmp/mt.tar.bz2
```

  * Копируем в домашнюю директорию http-сервера на плеере содержимое директории **/usr/local/etc/translate/www**:
```
cp -rf /usr/local/etc/translate/www /tmp_orig
cp -rf /usr/local/etc/translate/www /tmp
```

> _Замечание._ Перед модификацией **/tmp\_orig**, на плеере требуется разрешить запись в корень файловой системы (этот способ подходит только для прошивок с незащищенным от записи корневым разделом):
```
mount -o remount,rw /
```

> _Замечание_. На некоторых прошивках домашняя директория встроенного http-сервера может находится в **/usr/local/etc/www**.

  * В завершении добавляем дополнительный пункт в меню с интернет-сервисами:
```
<item>
  <title>Дополнительные сервисы</title>
  <link>rss_file://../etc/translate/rss/menuEx.rss</link>
  <media:thumbnail url="../etc/translate/rss/image/menuEx.png" width="120" height="90" />
  <mediaDisplay name=photoView />
</item>
```

> Пункт меню следует добавить в файл **/usr/local/etc/dvdplayer/savedrss/scripts/menu.rss**, если такого файла не существует, то его следует скопировать из **/usr/local/bin/scripts/menu.rss**:
```
mkdir -p /usr/local/etc/dvdplayer/savedrss/scripts
cp -i /usr/local/bin/scripts/menu.rss /usr/local/etc/dvdplayer/savedrss/scripts/menu.rss
```

## Вспомогательные утилиты ##

> Для полной работоспособности пакета дополнительно требуются следующие утилиты:

### [CURL](http://curl.haxx.se/) ###

> Необходима для работы с некоторыми online-сервисами, в частности [IVI.ru](http://ivi.ru).

> Входит в состав пакета **libcurl** для **[optware](http://www.nslu2-linux.org/wiki/Optware/HomePage)**.
```
ipkg install libcurl
```

> Путь к утилите **curl** прописывается в переменной CURL в **translate.conf**:
```
CURL=/opt/bin/curl
```

> Можно также воспользоваться статически слинкованной утилитой **[curl](http://media-translate.googlecode.com/files/curl.tar.bz2)**. Пример установки в **/usr/local/etc/translate/bin**:
```
cd /usr/local/etc/translate/bin
wget -O - http://media-translate.googlecode.com/files/curl.tar.bz2 | tar -xj
sed -i '/^CURL=/d' ../etc/translate.conf
echo -e '\nCURL=$BASEPATH/bin/curl' >> ../etc/translate.conf
```

### [XSLTPROC](http://xmlsoft.org/XSLT/) ###

> Требуется для быстрой обработки больших xml-файлов.

> Входит в состав пакета **xsltlib** для **[optware](http://www.nslu2-linux.org/wiki/Optware/HomePage)**.
```
ipkg install xsltlib
```

> Путь к утилите **xsltproc** прописывается в переменной XSLTPROC в **translate.conf**:
```
XSLTPROC=/opt/bin/xsltproc
```

> Можно также воспользоваться статически слинкованной утилитой **[xsltproc](http://media-translate.googlecode.com/files/xsltproc.tar.bz2)**. Пример установки в **/usr/local/etc/translate/bin**:
```
cd /usr/local/etc/translate/bin
wget -O - http://media-translate.googlecode.com/files/xsltproc.tar.bz2 | tar -xj
sed -i '/^XSLTPROC=/d' ../etc/translate.conf
echo -e '\nXSLTPROC=$BASEPATH/bin/xsltproc' >> ../etc/translate.conf
```

### [AWK](http://www.gnu.org/software/gawk/gawk.html) ###

> Требуется для нормальной работоспособности пакета. В случае, если интерпретатор отсутствует в прошивке необходимо установить его из **[optware](http://www.nslu2-linux.org/wiki/Optware/HomePage)**:
```
ipkg install gawk
```

> Можно также воспользоваться статически слинкованной утилитой **[awk](http://media-translate.googlecode.com/files/awk.tar.bz2)**. Пример установки в **/usr/local/etc/translate/bin**:
```
cd /usr/local/etc/translate/bin
wget -O - http://media-translate.googlecode.com/files/awk.tar.bz2 | tar -xj
```

### [RTMPDUMP](http://rtmpdump.mplayerhq.hu/) ###

> Альтернативная утилита для загрузки RTMP потока (вместо используемой по умолчанию **[flvstreamer](Introduction#%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82.md)**).

> Путь к утилите **rtmpdump** прописывается в переменной RTMPDUMP в **translate.conf**:
```
RTMPDUMP=/opt/bin/rtmpdump
```

> Можно воспользоваться статически слинкованной утилитой **[rtmpdump](http://code.google.com/p/eboda-hd-for-all-500/downloads/detail?name=rtmpdump)**. Пример установки в **/usr/local/etc/translate/bin**:
```
cd /usr/local/etc/translate/bin
wget -O - http://media-translate.googlecode.com/files/rtmpdump.tar.bz2 | tar -xj
sed -i '/^RTMPDUMP=/d' ../etc/translate.conf
echo -e '\nRTMPDUMP=$BASEPATH/bin/rtmpdump' >> ../etc/translate.conf
```

### [JS](http://www.ossp.org/pkg/lib/js/) ###

> Mozilla JavaScript Engine. Необходим для работы с некоторыми online-сервисами.

> Входит в состав пакета **ossp-js** для **[optware](http://www.nslu2-linux.org/wiki/Optware/HomePage)**.
```
ipkg install ossp-js
```

> Путь к утилите **js** прописывается в переменной JS в **translate.conf**:
```
JS=/opt/bin/js
```

> Можно также воспользоваться статически слинкованной утилитой **[js](http://media-translate.googlecode.com/files/js.tar.bz2)**. Пример установки в **/usr/local/etc/translate/bin**:
```
cd /usr/local/etc/translate/bin
wget -O - http://media-translate.googlecode.com/files/js.tar.bz2 | tar -xj
sed -i '/^JS=/d' ../etc/translate.conf
echo -e '\nJS=$BASEPATH/bin/js' >> ../etc/translate.conf
```


# Настройка #

  * Основной конфигурационный файл **/usr/local/etc/translate/etc/translate.conf**:
```
BASEPATH=/usr/local/etc/translate
export AWKPATH=$BASEPATH/lib:.

WGET=/usr/bin/wget
CURL=/opt/bin/curl
XSLTPROC=/opt/bin/xsltproc

STARTPOINT=$BASEPATH/etc/index.m3u
XSPFSCAN=$BASEPATH/etc/xspf.scan
MAINMENU=$BASEPATH/etc/menu/main.xspf

CACHEPATH=/tmp/cached

YOUTUBE_HD=yes
VIMEO_HD=yes
IVI_HD=yes
TVIGLE_HD=yes
NET_BANDWIDTH=

UDPXY_URL=http://127.0.0.1:8080/

TRANSLATE_CGI=http://127.0.0.1/cgi-bin/translate?
```

> Управление HD контентом для Youtube, Vimeo, Tvigle, Zoomby, ВКонтакте и IVI осуществляется с помощью переменных YOUTUBE\_HD, VIMEO\_HD, TVIGLE\_HD, ZOOMBY\_HD, VK\_HD и IVI\_HD соответственно.
> По умолчанию используется HD качество.

> TRANSLATE\_CGI содержит url на CGI-модуль **translate**. Путь должен заканчиваться символом '?'.

> STARTPOINT - содержит путь к стартовому файлу [XSPF Browser](ModuleXSPFBrowser.md).

  * Стартовый файл для [XSPF Browser](ModuleXSPFBrowser.md) **/usr/local/etc/translate/etc/index.m3u**:
```
#EXTM3U
#EXTINF:-1,Плеер HDD
/var/hdd/volumes/
#EXTINF:-1,Плеер USB
/var/ramfs/volumes/
#EXTINF:-1,Плеер Playlists
/usr/local/etc/playlist/
#EXTINF:-1,Плеер FTP
ftp://127.0.0.1/
```

_Замечание._ Все пути к директориям в плейлистах должны заканчиваться символом '/'.