<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:xspf="http://xspf.org/ns/0/"
  exclude-result-prefixes="xspf"
>

<xsl:output method="xml" encoding="utf-8" indent="yes"/>

<xsl:param name="title" />

<xsl:template match="/">
  <xsl:apply-templates select="stationlist"/>
</xsl:template>

<xsl:template match="stationlist">
	<channel>
		<title><xsl:value-of select="$title"/></title>
    <xsl:apply-templates select="station"/>
	</channel>
</xsl:template>

<xsl:template match="station">
  <item>
    <xsl:apply-templates select="@*"/>
  </item>
</xsl:template>

<xsl:template match="@*">
  <xsl:element name="{name()}">
    <xsl:value-of select="."/>
  </xsl:element>
</xsl:template>

<xsl:template match="*" />

</xsl:stylesheet>