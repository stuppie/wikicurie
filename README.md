# wikicurie

A python API for working with ID prefixes in the context of [prefixcommons](http://prefixcommons.org) and [Wikidata](http://www.wikidata.org)


E.g. [CHEBI:15377](www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:15377) <=> [P683](https://www.wikidata.org/wiki/Property:P683), 15377


The wikicurie.CurieUtil class provides CURIE/URI expansion/contraction
based on standard contexts.

See test_wikicurie.py for usage


### Future
There is a wikidata property `identifiers.org prefix (P4793)` that can
be used to link curie prefixes to wikidata pids. We still have the
non-standard formatting issues to deal with though (i.e. on DO, GO, ECO).