from saxonche import PySaxonProcessor

xml = "https://id.acdh.oeaw.ac.at/thun/editions/kaiser-an-thun-01-31-a3-xxi-d634.xml"

xslt = "https://tei4arche.acdh-dev.oeaw.ac.at/xsl/thun2arche.xsl"

with PySaxonProcessor(license=False) as proc:
    xsltproc = proc.new_xslt30_processor()
    document = proc.parse_xml(xml_uri=xml)
    executable = xsltproc.compile_stylesheet(stylesheet_file=xslt)
    output = executable.transform_to_string(xdm_node=document)
print(output)
