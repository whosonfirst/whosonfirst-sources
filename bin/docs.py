#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os
import logging
import datetime
import json
import io

if __name__ == '__main__':

    whoami = sys.argv[0]
    whoami = os.path.abspath(whoami)

    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    sources = os.path.join(root, 'sources')
    data = os.path.join(root, 'data')

    license = os.path.join(root, 'LICENSE.md')

    latest = os.path.join(data, "sources-spec-latest.json")
    readme = os.path.join(sources, "README.md")

    fh = io.open(latest, "r")
    spec = json.load(fh)

    now = datetime.datetime.now()
    ymd = now.strftime("%Y-%m-%d")

    lookup = {}

    for id, details in spec.items():
        lookup[details['name']] = id

    names = lookup.keys()
    names = sorted(names)

    #now write the license out
    _license = io.open(license, "w")
    _license.write("# License\n\n")

    _license.write("Crediting Who's On First is recommended and linking back to the License is required. For example:\n\n> Data from Who's On First. [License](https://whosonfirst.org/docs/licenses/).\n\nThe Who's On First dataset is both an original work and a modification of existing open data (sources listed below). Some of those open data projects do require attribution. We detail all sources and their specific license, usage, and vintage metadata in the full [sources list](https://whosonfirst.org/docs/sources/list/).\n\n")

    _license.write("_This file was generated by the `bin/docs.py` script on %s._\n\n" % ymd)

    docs = io.open(readme, "w")
    docs.write("# sources\n\n")

    docs.write("Crediting Who's On First is recommended and linking back to the License is required. For example:\n\n> Data from Who's On First. [License](https://whosonfirst.org/docs/licenses/).\n\nThe Who's On First dataset is both an original work and a modification of existing open data (sources listed below). Some of those open data projects do require attribution. We detail all sources and their specific license, usage, and vintage metadata in the full [sources list](https://whosonfirst.org/docs/sources/list/).\n\n")

    docs.write("_This file was generated by the `bin/docs.py` script on %s._\n\n" % ymd)

    source_count = 0
    source_via_count = 0
    source_concordance_count = 0

    for file in os.listdir(sources):
        if file.endswith('.json'):
            source_count += 1

    for n in names:

        id = lookup[n]
        details = spec[id]

        docs.write("## %s\n\n" % (details['fullname']))

        if details.get('description'):
            docs.write("_%s_ \n\n" % (details['description']))

        #call out mz associated sources (wof, transitland, etc)
        if details.get('mz_associated'):
            docs.write("_This is a Mapzen associated source._ \n\n")

        #call out add date
        if details.get('edtf:inception'):
            docs.write("* %s: `%s`\n" % ('added', details['edtf:inception']))

        #call out deprecated sources and their deprecated date
        if details.get('edtf:deprecated'):
            if not details['edtf:deprecated'] == 'uuuu':
                docs.write("* %s: `%s`\n" % ('deprecated', details['edtf:deprecated']))

        for k in ('id', 'name', 'prefix'):

            if details[k] == '':
                continue

            docs.write("* %s: `%s`\n" % (k, details[k]))

        if details.get('license_type'):
            docs.write("* %s: _%s_\n" % ('license_type', details['license_type']))

        if details.get('license_text'):
            docs.write("* %s: _%s_\n" % ('license_text', details['license_text']))

        if not details.get('url') == "":
            docs.write("* %s: _%s_\n" % ('url', details['url']))

        if details.get('remarks'):
            docs.write("* %s: _%s_\n" % ('remarks', details['remarks']))

        #link to the license page for each source if page is available
        if details.get('license') and details.get('license').startswith("http"):
            docs.write("* %s: _%s_\n" % ('license', details['license']))

        else:
            docs.write("* %s: `%s`\n" % ('license', details['license']))

        #list out all "via" sources with links to each source's source...
        has_via = False
        if details.get('src:via'):
            has_via = True

            docs.write("\n  This source includes `CC-BY compatible` data from the following organizations:\n")

            for via in details['src:via']:

                source_via_count += 1

                #if the source link is present, link to the source in markdown
                if not via['source_link'] == "":
                    if via['source_note']:
                        docs.write("  \t* **%s**: [%s](%s) - %s\n" % (via["context"],via["source_name"],via["source_link"],via["source_note"]))
                    else:
                        docs.write("  \t* **%s**: [%s](%s)\n" % (via["context"],via["source_name"],via["source_link"]))

                #if the source link is null for the src:via, write out just the name without a link
                else:
                    if via['source_note']:
                        docs.write("  \t* **%s**: %s - %s\n" % (via["context"],via["source_name"],via["source_note"]))
                    else:
                        docs.write("  \t* **%s**: %s\n" % (via["context"],via["source_name"]))

        #assuming no usage, appending to this empty list later if usage flags are present
        usage = []
        include_license = False

        #to construct the LICENSE page, we need to create variables for the license and url
        url = '[data](' + str(details['url']) + ')'
        license = '[license](' + str(details['license']) + ')'

        #catch any usage flag and append it as markdown to a usage: prop, if found
        if details.get('usage_concordance'):
            if details['usage_concordance'] == 1:
                usage.append("`concordance`")

        if details.get('usage_property'):        
            if details['usage_property'] == 1:
                usage.append("`property`")
                #if the source has a property usage, include in LICENSE
                include_license = True

        if details.get('usage_geometry'):
            if details['usage_geometry'] == 1:
                usage.append("`geometry`")
                #if the source has a property usage, include in LICENSE
                include_license = True

        all_uses = ', '.join(usage)

        if not usage == []:
            docs.write("* %s: %s\n" % ('usage', all_uses))

        #below, we need to list out some stats about sources
        #create a new variable, then subtract that from the over all source count
        if usage == ['`concordance`']:
            source_concordance_count +=1
        new_source_count = source_count - source_concordance_count

        docs.write("\n")

        #here, we're removing some sources from the license
        if str(details['license']) == 'N/A':
            include_license = False
        if str(details['license']) == 'N/A':
            include_license = False

        #if we don't have a useable url or license, don't set markdown in LICENSE
        if not str(details['url']).startswith('http'):
            url = 'data, '
        if not str(details['license']).startswith('http'):
            license = 'license, '

        #by now, we have sorted sources to include in the LICENSE, proceed...
        if include_license == True:

            if has_via == True:

                _license.write("- **" + str(details['fullname']) + "**: source " + url + ' and ' + license + '. This source includes `CC-BY` compatible data from the following organizations:\n')

                for via in details['src:via']:
                    _license.write("  - **" + via["context"] + "**: " + via["source_name"] + "\n")

            if not has_via == True:
                _license.write("- **" + str(details['fullname']) + "**: source " + url + ' and ' + license + '\n')

    #now write out the README and close all docs    
    docs.write("_All %s sources (%s primary sources, %s additional 'via' sources, and %s concordance-only sources) listed above are currently used to populate Who's On First records or will be added to Who's On First records in the near future._\n\n" % (source_count + source_via_count, new_source_count, source_via_count, source_concordance_count))
    _license.write("\n\n_All %s sources listed above are currently used to populate Who's On First records or will be added to Who's On First records in the near future._" % (new_source_count + source_via_count))

    docs.close()
    _license.close()
