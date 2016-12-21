class GrowingGraph:
    def __init__(self, neighbors_table, start_nodes):
        self.neighbors_table = neighbors_table
        self.outer_nodes = set(start_nodes)
        self.inner_nodes = set()

    def growing(self):
        for old_node in self.outer_nodes.copy():
            self._update_nodes(old_node)

    def _update_nodes(self, old_node):
        new_nodes = set(self.neighbors_table[old_node])
        if new_nodes:
            self.outer_nodes.remove(old_node)
            self.inner_nodes.add(old_node)
            for new_node in new_nodes:
                if new_node not in self.inner_nodes:
                    self.outer_nodes.add(new_node)

    def __str__(self):
        return 'GrowingGraph(out:{}, in:{})'.format(
            self.outer_nodes, self.inner_nodes
        )