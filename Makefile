spec:
	python ./bin/compile.py > data/sources-spec-`date "+%Y%m%d"`.json
	cp data/sources-spec-`date "+%Y%m%d"`.json data/sources-spec-latest.json