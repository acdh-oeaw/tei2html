from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from saxonche import PySaxonProcessor


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, tei: str | None = None, xslt: str | None = None):
    request_url = request.url._url
    print(request_url)
    if tei is None:
        tei = f"{request_url}static/tei.xml"
        print(tei)
    if xslt is None:
        xslt = f"{request_url}static/xslt.xsl"
    with PySaxonProcessor(license=False) as proc:
        xsltproc = proc.new_xslt30_processor()
        document = proc.parse_xml(xml_uri=tei)
        executable = xsltproc.compile_stylesheet(stylesheet_file=xslt)
        output = executable.transform_to_string(xdm_node=document)
    return HTMLResponse(content=output, status_code=200)
