# There are only two rules:
# 1. Variables at the top of the Makefile.
# 2. Targets are listed alphabetically. No, really.

WHOAMI = $(shell basename `pwd`)
YMD = $(shell date "+%Y%m%d")
PYTHON=$(shell which python3)

all: spec docs

docs:
	$(PYTHON) ./bin/docs.py

spec:
	$(PYTHON) ./bin/compile.py > data/sources-spec-`date "+%Y%m%d"`.json
	cp data/sources-spec-`date "+%Y%m%d"`.json data/sources-spec-latest.json
