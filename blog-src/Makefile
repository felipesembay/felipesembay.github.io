PELICAN = .venv/bin/pelican
PELICANOPTS =

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/../blog
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py

help:
	@echo "Comandos disponíveis:"
	@echo "  make html       - gera o blog localmente"
	@echo "  make serve      - sobe servidor local em :8000"
	@echo "  make publish    - gera versão de produção"
	@echo "  make github     - deploy no GitHub Pages"

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve: html
	@cd $(OUTPUTDIR) && python3 -m http.server 8000

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	.venv/bin/ghp-import -m "Publicar blog" -b gh-pages $(OUTPUTDIR)
	git push origin gh-pages

.PHONY: help html serve publish github
