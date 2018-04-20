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

    prefixes = {}
    names = {}

    required = ("id", "name", "prefix")

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

            for k in required:
                if not data.get(k, False):
                    logging.error("%s is missing a %s key" % (path, k))
                    sys.exit()

            name = data['name']
            prefix = data['prefix']

            if name in names:
                logging.error("%s is trying to claim name '%s' (already assigned to %s)" % (path, name, names[name]))

            if prefix in prefixes:
                logging.error("%s is trying to claim name '%s' (already assigned to %s)" % (path, prefix, prefixes[prefix]))

            names[ name ] = path
            prefixes[ prefix ] = path

            spec[data['id']] = data

    print json.dumps(spec)
    sys.exit(0)
