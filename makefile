# Author: Daniel Gisolfi 

repo=`grep __title__ ./mkp/__version__.py | grep -o '"[^"]\+"' | cut -d '"' -f2`
version=`grep __version__ ./mkp/__version__.py | grep -o '"[^"]\+"' | cut -d '"' -f2`

intro:
	@echo "$(repo) v$(version)"

init:
	@python3 -m pip install pipenv 
	@python3 -m pipenv install --dev

clean:
	-rm -rf ./build ./dist ./__pycache__/
	-rm -rf ./$(repo)/$(repo).egg-info ./.eggs ./$(repo).egg-info
	-rm -f *.pyc *.pyo *.pyd *\$$py.class
	-rm -rf ./doc

test:
	@python3 -m pytest -W 

build: init doc
	-pipenv run pipenv-setup sync
	@python3 setup.py sdist bdist_wheel

publish:
	@python3 -m twine upload dist/*

install:
	@python3 -m pip install .

uninstall:
	@python3 -m pip uninstall $(repo)==$(version)

sort_imports:
	isort -rc --atomic .
	# if this fails run pipenv shell and install dev 

MAKE:
	intro
	build
	install

.PHONY: intro init clean test build publish install uninstall sort_imports