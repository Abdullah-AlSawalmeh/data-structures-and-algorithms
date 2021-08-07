from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value) # O(1)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

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


    def breadth_first(self,node):
        queue = Queue()
        queue.enqueue(node)
        visited  = set()
        visited.add(node)
        node_list = []
        def inner_func(queue,visited,node_list):
            for index in range(len(queue)):
                node = queue.dequeue()
                node_list.append(node)
                neighbors = self.get_neighbors(node)
                for edge in neighbors:
                    if edge[0] not in visited:
                        queue.enqueue(edge[0])
                        visited.add(edge[0])
            if len(queue) > 0:
                inner_func(queue,visited,node_list)
        inner_func(queue,visited,node_list)
        return node_list

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list:
            # print(vertix.value)
            print(f' \n {vertix.value} ==>')
            for i in self.adjacency_list.get(vertix):
                print(i[0].value, end = ' ')

        return output

    def depth_first(self, start_node):
        nodes = []
        depth = []
        visited = []

        if start_node not in self.adjacency_list:
            raise ValueError
        
        depth.append(start_node)

        while not depth == []:
            top_node = depth.pop(0)
            nodes.append(top_node.value)
            top_node_neighbors = self.get_neighbors(top_node)

            for neighbor in top_node_neighbors[::-1]:
                if neighbor[0] not in visited:
                    visited.append(top_node)
                    visited.append(neighbor[0])
                    depth.append(neighbor[0])

        return nodes



if __name__ == '__main__':
    # graph = Graph()
    # a = graph.add_node('a')
    # b = graph.add_node('b')
    # c = graph.add_node('c')
    # d = graph.add_node('d')
    # e = graph.add_node('e')
    # f = graph.add_node('f')
    # g = graph.add_node('g')
    # h = graph.add_node('h')
    # i = graph.add_node('i')
    # k = graph.add_node('k')
    # graph.add_edge(a, b)
    # graph.add_edge(a, c)
    # graph.add_edge(a,e)
    # graph.add_edge(b, d)
    # graph.add_edge(c, f)
    # graph.add_edge(c, b)
    # graph.add_edge(e,g)
    # graph.add_edge(f,h)
    # graph.add_edge(g,h)
    # graph.add_edge(f,i)
    # graph.add_edge(h,k)
    # graph.add_edge(i,k)
    # # print(graph.breadth_first(a)[0].value)
    # # print(graph.breadth_first(a)[1].value)
    # # print(graph.breadth_first(a)[2].value)
    # # print(graph.breadth_first(a)[3].value)
    

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
    print(len(graph.breadth_first(a)))
# 
#     print(graph)
    # print(graph.adjacency_list)