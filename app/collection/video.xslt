<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:xspf="http://xspf.org/ns/0/"
  exclude-result-prefixes="xspf"
>

<xsl:output method="xml" encoding="utf-8" indent="yes"/>

<xsl:template match="/">
  <xsl:apply-templates select="xspf:playlist"/>
</xsl:template>

<xsl:template match="xspf:playlist">
	<channel>
		<title><xsl:value-of select="xspf:title"/></title>
    <xsl:apply-templates select="xspf:trackList/xspf:track"/>
	</channel>
</xsl:template>

<xsl:template match="xspf:track">
  <item>
    <xsl:apply-templates select="xspf:*"/>
  </item>
</xsl:template>

<xsl:template match="xspf:meta">
  <xsl:element name="{@rel}">
    <xsl:value-of select="."/>
  </xsl:element>
</xsl:template>

<xsl:template match="xspf:*">
  <xsl:element name="{name()}">
    <xsl:value-of select="."/>
  </xsl:element>
</xsl:template>

<xsl:template match="*" />

</xsl:stylesheet>