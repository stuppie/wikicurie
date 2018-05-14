from .curie_map import curie_map as default_curie_map


class CurieUtil(object):
    def __init__(self, curie_map=None):
        if not curie_map:
            curie_map = default_curie_map
        for k, v in curie_map.items():
            if 'formatter' not in v:
                v['formatter'] = '{}'
            if 'reverse_formatter' not in v:
                v['reverse_formatter'] = '{}'
            if not (isinstance(v['formatter'], str) or hasattr(v['formatter'], '__call__')):
                raise ValueError(v['formatter'])
            if not (isinstance(v['reverse_formatter'], str) or hasattr(v['reverse_formatter'], '__call__')):
                raise ValueError(v['reverse_formatter'])
        self.curie_map = curie_map
        self.prop_curie = {v['pid']: k for k, v in curie_map.items()}

    def parse_curie(self, curie: str):
        """
        Given a curie (e.g. CHEBI:1234), return the wikidata property and formatted value
        :param curie:
        :return:
        """
        if curie.count(':') != 1:
            raise ValueError("There must be one ':' in the curie: {}".format(curie))
        ns, value = curie.split(':')
        if ns not in self.curie_map:
            raise ValueError("Unknown namespace: {}".format(ns))
        cm = self.curie_map[ns]

        wikidata_value = None
        if isinstance(cm['formatter'], str):
            wikidata_value = cm['formatter'].format(value)
        elif hasattr(cm['formatter'], '__call__'):
            wikidata_value = cm['formatter'](value)
        return cm['pid'], wikidata_value

    def make_curie(self, pid: str, value: str):
        """
        Given a pid (e.g. P699) and a value (e.g. DOID:1234, this value comes from wikidata!!), return the curie
        :param pid:
        :param value:
        :return:

        print(cu.make_curie("P699", "DOID:1234")) --> "DOID:1234"
        print(cu.make_curie("P698", "1234")) --> PUBMED:1234
        """
        if pid not in self.prop_curie:
            return None
        ns = self.prop_curie[pid]
        cm = self.curie_map[ns]

        curie_value = None
        if isinstance(cm['reverse_formatter'], str):
            curie_value = cm['reverse_formatter'].format(value)
        elif hasattr(cm['reverse_formatter'], '__call__'):
            curie_value = cm['reverse_formatter'](value)
        return ns + ':' + curie_value

    @staticmethod
    def uri_to_curie(uri: str):
        """
        converts a URI to a curie. Does not need to understand anything about the namespace
        function simply take everything after the last underscore as the 'value', and the
        string between the last '/' and the '_' as the namespace.
        Throws an exception if there are no slashes or semicolons
        """
        assert "/" in uri, "No '/' found in {}".format(uri)
        end_uri = uri.split("/")[-1]
        assert end_uri.count("_") == 1, "No '_' found in {} ({})".format(end_uri, uri)
        curie = end_uri.replace("_", ":")
        return curie

    def is_valid_namespace(self, namespace: str):
        """
        check if the namespace exists in the curie_map
        """
        return namespace in self.curie_map