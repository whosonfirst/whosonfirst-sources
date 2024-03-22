# whosonfirst-sources

Where things come from in Who's On First.

Click [here](sources/README.md) to see a full list of Who's On First sources.

## Adding a new source

1. Create a new source `{SOURCE}.json` file using the [template file](source_template.json) where `{SOURCE}` should be the same as the `prefix` property of the source itself.
2. Fill out all required properties and optional properties, if available.
3. Run the [Makefile](Makefile) using the `make all` command.

## Source Properties

While a source .json file in the `whosonfirst-sources` repository does not require all properties listed below, the more information we are able to gather about a source, the better. When adding a new source, please provide as much current, available information about that specific source as possible.

* `"id":` A unique numeric integer identifier, typically derived from [Brooklyn Integers](https://www.brooklynintegers.com) (_integer, required property_).

* `"fullname":` The full name of the source (_string, required property_).

* `"name":` The user-derived, abbrviated name of a given source (_string, required property_).

* `"prefix":` The user-derived, prefix a given source. This value is typically two to ten characters in length (_string, required property_).

* `"key":` A list of data properties used from the source. Optional and typically left empty (_string, optional property_).

* `"url":`  An http link to the source, preferably the homepage (_string, optional property_).

* `"license":` A link to the license or terms of service page, if available, for the source (_string, optional property_).

* `"license_type":` The license or equivalent license type for the source's data (_string, optional property_).

* `"license_text":` A one to two sentence description of what the license allows (_string, optional property_).

* `"license_text_eng":` A one to two sentence description of what the license allows, in English. Used when the `license_text` is non-English (_string, optional property_).

* `"src:via"`: A list of sources used by a source. A list of key/value pairs that includes the source context, source name, link to the source website, and a note about the source (_list, optional property_). See the [template file](source_template.json) for an example.

* `"usage_concordance":` Represents whether or not this source is used for concordance values (_integer, required property_). `1` value indicates use, `0` value indicates no use, `-1` value indicates unsure of use.

* `"usage_property":` Represents whether or not this source is used for property values (_integer, required property_). `1` value indicates use, `0` value indicates no use, `-1` value indicates unsure of use.

* `"usage_geometry":` Represents whether or not this source is used for geometries (_integer, required property_). `1` value indicates use, `0` value indicates no use, `-1` value indicates unsure of use.

* `"description":` A one to two sentence description of the source (_string, optional property_).

* `"mz:is_current":` Represents whether of not a source is currently in use (_integer, optional property_). `0` signifies "not current".

* `"mz:associated":` Represents a source associated with works at Mapzen (_integer, optional property_). `1` signifies "Mapzen associated".

* `"edtf:deprecated":` Indicates the date when a source was determined to be invalid, was never a "going concern" (_string, optional property_). _Format: YYYY-MM-DD (though these dates can be encoded with any valid EDTF syntax)_.

* `"edtf:inception":` Indicates the date when a source was added to Who's On First. (_string, required property_). _Format: YYYY-MM-DD (though these dates can be encoded with any valid EDTF syntax)_.

## See also

* https://github.com/whosonfirst
* https://github.com/whosonfirst-data
