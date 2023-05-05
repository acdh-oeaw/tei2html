[![Build and publish Docker image](https://github.com/acdh-oeaw/tei2html/actions/workflows/build.yml/badge.svg)](https://github.com/acdh-oeaw/tei2html/actions/workflows/build.yml)
[![flake8 Lint](https://github.com/acdh-oeaw/tei2html/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/tei2html/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/tei2html/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/tei2html/actions/workflows/test.yml)
# tei2html

a [fastapi](https://fastapi.tiangolo.com/) service to transform XML documents via XSLT into HTML


## docker

* `docker build -t tei2html .`
* `docker run -d --name tei2html -p 8020:8020 tei2html`