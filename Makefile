# There are only two rules:
# 1. Variables at the top of the Makefile.
# 2. Targets are listed alphabetically. No, really.

WHOAMI = $(shell basename `pwd`)
YMD = $(shell date "+%Y%m%d")

all: spec docs

archive: all
	tar --exclude='.git*' --exclude='Makefile*' -cvjf $(dest)/$(WHOAMI)-$(YMD).tar.bz2 ./bin ./data ./sources ./LICENSE.md ./CONTRIBUTING.md ./README.md

docs:
	${PYTHON} ./bin/docs.py

# https://internetarchive.readthedocs.org/en/latest/cli.html#upload
# https://internetarchive.readthedocs.org/en/latest/quickstart.html#configuring

ia:
	ia upload $(WHOAMI)-$(YMD) $(src)/$(WHOAMI)-$(YMD).tar.bz2 --metadata="title:$(WHOAMI)-$(YMD)" --metadata="licenseurl:http://creativecommons.org/licenses/by/4.0/" --metadata="date:$(YMD)" --metadata="subject:geo;mapzen;whosonfirst" --metadata="creator:Who's On First (Mapzen)"

internetarchive:
	$(MAKE) dest=$(src) archive
	$(MAKE) src=$(src) ia
	rm $(src)/$(WHOAMI)-$(YMD).tar.bz2

spec:
	${PYTHON} ./bin/compile.py > data/sources-spec-`date "+%Y%m%d"`.json
	cp data/sources-spec-`date "+%Y%m%d"`.json data/sources-spec-latest.json
