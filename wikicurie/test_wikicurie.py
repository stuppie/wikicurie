from .wikicurie import CurieUtil

cu = CurieUtil()


def test_doid_to_wd():
    # wikidata stores the "DOID:" part as part of the value for this property
    curie = "DOID:1234"
    pid, value = cu.parse_curie(curie)
    assert pid == "P699"
    assert value == "DOID:1234"


def test_wd_to_doid():
    pid = "P699"
    value = "DOID:1234"
    curie = cu.make_curie(pid, value)
    assert curie == "DOID:1234"


def test_pmid_to_wd():
    # wikidata does not store the "PUBMED:" part as part of the value for this property
    curie = "PUBMED:1234"
    pid, value = cu.parse_curie(curie)
    assert pid == "P698"
    assert value == "1234"


def test_wd_to_pmid():
    pid = "P698"
    value = "1234"
    curie = cu.make_curie(pid, value)
    assert curie == "PUBMED:1234"
