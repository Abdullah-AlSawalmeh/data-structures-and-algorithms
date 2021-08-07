from graphs.graphs import *

def depth_first(self, start_node):
    nodes = []
    depth = []

    if start_node not in self.adjacency_list:
        raise ValueError
    
    depth.append(start_node)

    while not depth == []:
        top_node = depth.pop(0)
        nodes.append(top_node.value)
        top_node_neighbors = self.get_neighbors(top_node)

        for neighbor in top_node_neighbors[::-1]:
            if not neighbor[0].visited:
                top_node.visited = True
                neighbor[0].visited = True

                depth.append(neighbor[0])

    for node in self.adjacency_list:
        node.visited = False

    return nodes