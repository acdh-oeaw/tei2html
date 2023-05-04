from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from saxonche import PySaxonProcessor


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root(tei: str, xslt: str):
    with PySaxonProcessor(license=False) as proc:
        xsltproc = proc.new_xslt30_processor()
        document = proc.parse_xml(xml_uri=tei)
        executable = xsltproc.compile_stylesheet(stylesheet_file=xslt)
        output = executable.transform_to_string(xdm_node=document)
    return HTMLResponse(content=output, status_code=200)
