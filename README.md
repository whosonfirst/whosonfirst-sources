# whosonfirst-sources

Where things come from in Who's On First.

## Source Example

**See:** The `whosonfirst-sources` [template file](https://github.com/whosonfirst/whosonfirst-sources/blob/master/source_template.json) when adding a new source.

#### Atlanta Department of Planning and Community Development

_Neighborhoods within the City of Atlanta._

* id `1108797031`
* name `atldpcd`
* prefix `atldpcd`
* license_type _CC BY 4.0_
* license_text _Share, copy and redistribute the material in any medium or format. Adapt, remix, transform, and build upon the material for any purpose, even commercially._
* url _http://dpcd.coaplangis.opendata.arcgis.com/datasets/neighborhoods_
* license _https://www.arcgis.com/home/item.html?id=716f417a1990446389ef7fd2c381d09f_


### Source Properties

While a source .json file in the `whosonfirst-sources` repository does not require all properties listed below, the more information we are able to gather about a source, the better. When adding a new source, please provide as much current, available information about that specific source as possible.

* `"id":` A unique numeric integer identifier, typically derived from [Brooklyn Integers](https://www.brooklynintegers.com) (_integer, required property_).

* `"fullname":` The full name of the source (_string, required property_).

* `"name":` The user-derived, abbrviated name of a given source. (_string, required property_).

* `"prefix":` The user-derived, prefix a given source. This value is typically two to ten characters in length (_string, required property_).

* `"key":` A list of data properties used from the source. Optional and typically left empty (_string, optional property_).

* `"url":`  An http link to the source, preferably the homepage (_string, optional property_).

* `"license":` A link to the license or terms of service page, if available, for the source (_string, optional property_).

* `"license_type":` The license or equivalent license type for the source's data (_string, optional property_).

* `"license_text":` A one to two sentence description of what the license allows (_string, optional property_).

* `"description":` A one to two sentence description of the source (_string, optional property_).


## See also

* https://github.com/whosonfirst
