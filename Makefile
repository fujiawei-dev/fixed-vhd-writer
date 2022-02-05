.PHONY: ;
.SILENT: ;               # no need for @
.ONESHELL: ;             # recipes execute in same shell
.NOTPARALLEL: ;          # wait for target to finish
.EXPORT_ALL_VARIABLES: ; # send all vars to shell

.IGNORE: dep clean test;            # ignore all errors, keep going

ifeq ($(OS), Windows_NT)
SHELL := pwsh.exe
.SHELLFLAGS := -NoProfile -Command
endif

VERSION = 0.0.1
PACKAGE = fixed-vhd-writer

all: reinstall test

dep:
	pip install -r requirements.txt

build:
	python setup.py sdist
	python setup.py bdist_wheel

uninstall:
	pip uninstall -y $(PACKAGE)

install: uninstall build
	pip install --force-reinstall --no-deps dist/$(PACKAGE)-$(VERSION).tar.gz

reinstall: install clean

upload: build
	twine upload dist/$(PACKAGE)-$(VERSION).tar.gz

test:
	pytest
	rm -r .pytest_cache

clean:
	rm -r build
	rm -r dist
	rm -r *egg-info

tag:
	git tag v$(VERSION)
	git push origin v$(VERSION)