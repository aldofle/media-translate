<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:xspf="http://xspf.org/ns/0/"
  xmlns:str="http://exslt.org/strings"
  extension-element-prefixes="str"
  exclude-result-prefixes="xspf"
>

<!--
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
-->

<xsl:output method="xml" encoding="utf-8" indent="yes"/>

<xsl:template match="/">
  <xsl:apply-templates select="genrelist"/>
</xsl:template>

<xsl:template match="genrelist">
    <channel>
	<title>Shoutcast Radio Genre List</title>
	<xsl:apply-templates select="genre"/>
    </channel>
</xsl:template>

<xsl:template match="genre">
<item>
<name><xsl:value-of select="@name"/></name>
<link>http://127.0.0.1/cgi-bin/translate?app,<xsl:value-of select="str:encode-uri(@name, true())" />,shoutcast/genre</link>
</item>
</xsl:template>

<xsl:template match="*" />

</xsl:stylesheet>