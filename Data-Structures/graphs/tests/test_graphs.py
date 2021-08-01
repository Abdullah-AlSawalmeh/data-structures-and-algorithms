from graphs.graphs import *
import pytest

"""
Test Cases:
    Node can be successfully added to the graph
    An edge can be successfully added to the graph
    A collection of all nodes can be properly retrieved from the graph
    All appropriate neighbors can be retrieved from the graph
    Neighbors are returned with the weight between nodes included
    The proper size is returned, representing the number of nodes in the graph
    A graph with only one node and edge can be properly returned
    An empty graph properly returns null
"""

def test_add_node():
    graph = Graph()
    assert graph.add_node('abdullah').value == 'abdullah'

def test_size_empty():
    graph = Graph()
    assert graph.size() == 0


def test_size():
    graph = Graph()
    graph.add_node('abdullah')
    assert graph.size() == 1

    graph.add_node('sawalmeh')
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
    end = graph.add_node('abdullah')
    start = graph.add_node('sawalmeh')
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

