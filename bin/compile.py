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
    spec = {}

    for (root, dirs, files) in os.walk(sources):

        for f in files:
    
            path = os.path.join(root, f)

            if not path.endswith('.json'):
                continue

            try:
                fh = open(path, 'r')
                data = json.load(fh)
            except Exception, e:
                logging.error("failed to parse %s, because %s" % (path, e))
                sys.exit()

            spec[data['id']] = data

    print json.dumps(spec)
    sys.exit()
