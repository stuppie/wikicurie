"""
curie_map is a map of prefixes to metadata

Prefixes match the prefixes in https://github.com/prefixcommons/biocontext/blob/master/registry/uber_context.jsonld

values:
pid: URI for the Wikidata property
uri: an external URI (optional, not currently used for anything)
formatter: a string formatter or function that is used to convert the curie value to wikidata value (default: '{}')
reverse_formatter: a string formatter or function that is used to convert the wikidata value to curie value  (default: '{}')

Example:

"""

curie_map = {
    'GO': {
        'pid': 'P686',
        'uri': 'http://purl.obolibrary.org/obo/GO_',
        'formatter': 'GO:{}',
        'reverse_formatter': lambda s: s.replace("GO:", "")
    },
    'NCBITaxon': {
        'pid': 'P685',
    },
    'NCBIGENE': {
        'uri': 'http://www.ncbi.nlm.nih.gov/gene/',
        'pid': 'P351',
    },
    'UNIPROT': {
        'uri': 'http://identifiers.org/uniprot/',
        'pid': 'P352',
    },
    'HGNC.SYMBOL': {
        'pid': 'P353',
    },
    'HGNC': {  # hgnc id
        'uri': 'http://identifiers.org/hgnc/',
        'pid': 'P354',
    },
    'DOID': {
        'uri': 'http://purl.obolibrary.org/obo/DOID_',
        'pid': 'P699',
        'formatter': 'DOID:{}',
        'reverse_formatter': lambda s: s.replace("DOID:", "")
    },
    'OMIM': {
        'uri': 'http://purl.obolibrary.org/obo/OMIM_',
        'pid': 'P492'
    },
    'MESH': {
        'uri': 'http://purl.obolibrary.org/obo/MESH_',
        'pid': 'P486'
    },
    'UMLS': {
        'uri': 'http://purl.obolibrary.org/obo/UMLS_',
        'pid': 'P2892'
    },
    'ECO': {
        'uri': 'http://purl.obolibrary.org/obo/ECO_',
        'pid': 'P3811',
        'formatter': 'ECO:{}',
        'reverse_formatter': lambda s: s.replace("ECO:", "")
    },
    'PUBMED': {
        'uri': 'http://www.ncbi.nlm.nih.gov/pubmed/',
        'pid': 'P698',
    },
    'DOI': {
        'uri': 'http://dx.doi.org/',
        'pid': 'P356',
    },
    'CHEBI': {
        'uri': 'http://purl.obolibrary.org/obo/CHEBI_',
        'pid': 'P683',
    },
    'DRUGBANK': {
        'uri': 'http://www.drugbank.ca/drugs/',
        'pid': 'P715',
    },
    'RXNORM': {
        'uri': 'http://purl.bioontology.org/ontology/RXNORM/',
        'pid': 'P3345',
    },
    'UNII': {
        'uri': 'http://fdasis.nlm.nih.gov/srs/unii/',
        'pid': 'P652',
    },
    'CAS': {
        'uri': 'http://identifiers.org/cas/',
        'pid': 'P231',
    },
    'CHEMBL.COMPOUND': {
        'uri': 'http://identifiers.org/chembl.compound/',
        'pid': 'P592',
        'formatter': "{}",
        'reverse_formatter': lambda s: s.replace("CHEMBL", ''),
    },
    'ICD9': {
        'pid': 'P493',
    },
    'ICD10': {
        'pid': 'P494',
    },
    'ICD10CM': {
        'pid': 'P4229',
    },
    'ICD9CM': {
        'pid': 'P1692'
    },
    'wd': {
        'uri': 'http://www.wikidata.org/entity/',
        'pid': 'http://www.wikidata.org/entity/',  # placeholder
    }
}
