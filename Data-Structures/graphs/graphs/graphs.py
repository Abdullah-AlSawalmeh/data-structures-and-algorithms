class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []

        return node

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self.adjacency_list:
            raise KeyError('does not exist.')

        if end_node not in self.adjacency_list:
            raise KeyError('does not exist.')

        adjacencies = self.adjacency_list[start_node]
        adjacencies.append((end_node, weight))

    def get_nodes(self):
        return self.adjacency_list.keys()


    def size(self):
        return len(self.adjacency_list)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]


    def __str__(self):
        output = ''
        for vertix in self.adjacency_list:
            # print(vertix.value)
            print(f' \n {vertix.value} ==>')
            for i in self.adjacency_list.get(vertix):
                print(i[0].value, end = ' ')

        return output



if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)

    print(graph)
    # print(graph.adjacency_list)