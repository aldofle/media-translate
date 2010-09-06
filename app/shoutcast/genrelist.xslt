<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:xspf="http://xspf.org/ns/0/"
  exclude-result-prefixes="xspf"
>

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
    <title><xsl:value-of select="@name"/></title>
  </item>
</xsl:template>

<xsl:template match="*" />

</xsl:stylesheet>