# Назначение #

RSS/CGI-модуль предназначен для управления проигрыванием медиапотоков на плеере с локального компьютера.

Адрес web-интерфейса: `http://<player_ip>/cgi-bin/renderer`

# Детали #

Управление осуществляется следующими get запросами на плеер:
```
http://<player_ip>/cgi-bin/translate?renderer,[<options>],<stream_url>
http://<player_ip>/cgi-bin/translate?renderer-stop,,
http://<player_ip>/cgi-bin/translate?renderer-pause,,
http://<player_ip>/cgi-bin/translate?renderer-play,,
```

## Add-on для интернет браузеров ##

Для удобства работы можно загрузить и установить расширение **Play on Player** для интернет браузера, которые добавляют кнопки в popup-меню и тулбар браузера.

### Firefox ###

Установка для Firefox:
  1. cкачиваем `http://<player_ip>/bin/playonplayer.xpi`;
  1. кидаем xpi в окно Firefox для установки расширения;
  1. после перезагрузки браузера следует выставить IP адрес или имя плеера в опциях расширения (по умолчанию player).

Удаление для Firefox:
  1. Стандартным способом из диалога Инструменты/Дополнения.

### Google Chrome ###

Установка для Google Chrome:
  1. cкачиваем `http://<player_ip>/bin/playonplayer.crx`;
  1. в настройках add-on следует выставить IP адрес или имя плеера (по умолчанию player).

Удаление для Google Chrome:
  1. Стандартным способом из диалога Инструменты/Дополнения.

### Internet Explorer ###

Установка для Internet Explorer:
  1. cкачиваем `http://<player_ip>/bin/playonplayer.exe`;
  1. запускаем его для установки расширения;
  1. IP адрес или имя плеера надо будет поменять в реестре HKEY\_LOCAL\_MACHINE\SOFTWARE\RSSEx\PlayerIP.

Удаление для Internet Explorer:
  1. Стандартным способом из Панель Управления/Установка и удаление программ.

## Использование ##

  1. Кликаем правой кнопкой мыши по ссылке, которую хотим проиграть и выбираем пункт **Play on Player** (**Проиграть на Плеере**). Если ссылка не будет найдена в качестве ссылки для проигрывания будет использован адрес текущей страницы в браузере. Для IE помимо ссылки можно также кликать и на выделенный текст. В этом случае содержимое выделения будет рассматриваться как ссылка для проигрывания;
  1. Находясь на странице поддерживаемого контент провайдера с нужным нам контентом нажимаем на тулбаре кнопку **Play on Player** (**Проиграть на Плеере**);
  1. Из web-интерфейса Media Stream Renderer вводим ссылку для проигрывания в поле **Stream URL** и нажимаем **Submit**;
  1. Из web-интерфейса Media Stream Renderer есть возможность удаленно управлять проигрыванием медиапотока на плеере **Stop/Pause/Play**;
  1. Ссылки на плейлисты и медиа RSS (вебкасты, подкасты и тп) перенаправляются в модуль XSPF Browser;
  1. В режиме ожидания можно повторно запустить на проигрывание предыдущий медиа поток командой **Play** из web-интерфейса или с пульта.