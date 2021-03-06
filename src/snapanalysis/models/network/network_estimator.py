import networkx as nx

class NetworkEstimator(object):

    _data = None

    def fit(self, data):
        self._data = data

    def to_network(self, threshold, additional_attributes=None):
        """
        Returns networkx network of the graph generated by the method, thresholded at threshold
        :param threshold: threshold to put on the adjacency matrix (adjacencies > threshold will have an edge)
        :param additional_attributes: other attributes to apply to edges (dict)
        :return:
        """
        graph = nx.Graph()

        for node in self._data.index:
            graph.add_node(node)

        adjacency = self.adjacency_
        true_interactions = adjacency > threshold
        # leave only the ones that have interaction=True
        adjacency = adjacency[true_interactions]

        if additional_attributes is None:
            additional_attributes = {}

        for (node_a, node_b), weight in adjacency.iteritems():
            kwargs = additional_attributes.get((node_a, node_b), {})

            graph.add_edge(node_a, node_b, weight=weight, **kwargs)

        return graph

    def p_values(self):
        raise NotImplementedError