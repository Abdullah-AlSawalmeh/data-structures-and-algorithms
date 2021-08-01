from graphs.graphs import *
import pytest

"""
Test Cases:
    1. Can create a Graph.
    2. Can add a node.
    3. Can get size.
    4. Can add edge between two nodes.
    5. Can add multiple edges.
    6. Can get list of nodes in the graph with their weights.
    7. Can get list of neighbor-nodes of a specific nodes.
    8. Can return True is there is a path between two nodes.
    9. Can return False is there is no path between two nodes.
"""

def test_add_node():
    graph = Graph()
    assert graph.add_node('batool').value == 'batool'

def test_size_empty():
    graph = Graph()
    assert graph.size() == 0


def test_size():
    graph = Graph()
    graph.add_node('batool')
    assert graph.size() == 1

    graph.add_node('malkawi')
    assert graph.size() == 2


def test_edge_start_node_not_in_graph():
    graph = Graph()
    start = Node('start')
    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_edge_end_node_not_in_graph():
    graph = Graph()
    end = Node('end')
    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_one_edge():
    graph = Graph()
    end = graph.add_node('end')
    start = graph.add_node('start')
    graph.add_edge(start, end)

def test_add_edge():
    graph = Graph()
    end = graph.add_node('batool')
    start = graph.add_node('malkawi')
    graph.add_edge(start, end)
    assert graph.adjacency_list[start][0] == (end, 1)
    assert graph.get_neighbors(start) == [(end, 1)]
    graph.add_edge(end, start)
    assert graph.get_neighbors(end) == [(start, 1)]


def test_get_nodes():
    graph = Graph()
    banana = graph.add_node('banana')
    apple = graph.add_node('apple')
    dog = graph.add_node('dog')
    assert len(graph.get_nodes()) == 3

def test_get_nodes_empty():
    graph = Graph()
    assert len(graph.get_nodes()) == 0

def test_get_neighbors():
    graph = Graph()
    banana = graph.add_node('banana')
    apple = graph.add_node('apple')
    graph.add_edge(apple, banana, 5)
    neighbors = graph.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0][0].value == 'banana'
    assert isinstance(neighbors[0][0], Node)
    assert neighbors[0][1] == 5

def test_get_neighbors_no_neighbors():
    graph = Graph()
    banana = graph.add_node('banana')
    neighbors = graph.get_neighbors(banana)
    assert len(neighbors) == 0
    assert neighbors == []

def test_is_path_bfs_true():
    graph = Graph()
    n1 = graph.add_node(1)
    n2 = graph.add_node(2)
    graph.add_edge(n1, n2)
    assert (graph.isPathBFS(n1, n2)) == True

def test_is_path_bfs_false():
    graph = Graph()
    n1 = graph.add_node(1)
    n2 = graph.add_node(2)
    graph.add_edge(n1, n2)
    assert (graph.isPathBFS(n2, n1)) == False
