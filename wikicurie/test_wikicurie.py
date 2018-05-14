from .wikicurie import CurieUtil
import unittest

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


class MyTestCase(unittest.TestCase):
    def test_uri_to_curie(self):
        uri = "http://purl.obolibrary.org/obo/UBERON_0026700"
        assert cu.uri_to_curie(uri) == "UBERON:0026700"

        with self.assertRaises(Exception):
            cu.uri_to_curie("http://purl.bioontology.org/ontology/provisional/f17c9aff-4a92-418e-989f-b8e9dd62caf6")
