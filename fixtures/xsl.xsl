<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">
    <xsl:output method="html" encoding="utf-8" indent="yes" />
    <xsl:template match="/">
        <xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html&gt;</xsl:text>
        <html lang="en">
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>

                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
                    rel="stylesheet"
                    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
                    crossorigin="anonymous"/>

                <title><xsl:value-of select=".//tei:title[1]/text()"/></title>
            </head>
            <body>
                <h1><xsl:value-of select=".//tei:title[1]/text()"/></h1>
                <xsl:apply-templates select=".//tei:body"/>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"/>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="tei:p">
        <p><xsl:apply-templates/></p>
    </xsl:template>
</xsl:stylesheet>
