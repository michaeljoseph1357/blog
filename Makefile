PY=python3
PELICAN?=pelican
PELICANOPTS=

help:
	@echo 'make dev        -> serve with autoreload'
	@echo 'make build      -> build to ./output'
	@echo 'make publish    -> build with publishconf.py'
	@echo 'make clean      -> remove output'

dev:
	$(PELICAN) -lr $(PELICANOPTS) -s pelicanconf.py

build:
	$(PELICAN) content -o output -s pelicanconf.py

publish:
	$(PELICAN) content -o output -s publishconf.py

clean:
	rm -rf output
