#!/usr/bin/env python

import os
import sys
import logging

import json

if __name__ == '__main__':

    whoami = sys.argv[0]
    whoami = os.path.abspath(whoami)
    
    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    sources = os.path.join(root, 'sources')
    data = os.path.join(root, 'data')

    latest = os.path.join(data, "sources-spec-latest.json")
    readme = os.path.join(sources, "README.md")

    fh = open(latest, "r")
    spec = json.load(fh)

    lookup = {}

    for id, details in spec.items():
        lookup[details['name']] = id

    names = lookup.keys()
    names.sort()

    docs = open(readme, "w")
    docs.write("# sources\n\n")
    
    for n in names:

        id = lookup[n]
        details = spec[id]

        docs.write("## %s\n\n" % (details['fullname']))

        if details.get('description'):
            docs.write("_%s_\n\n" % (details['description']))

        for k in ('id', 'name', 'prefix', 'url', 'license'):
            docs.write("* %s `%s`\n" % (k, details[k]))

        docs.write("\n")

    docs.close()
        

