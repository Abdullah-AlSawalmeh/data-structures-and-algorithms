from graphs.graphs import *
from depth_first.depth_first import *
import pytest

def test_depth_first_empty_graph():
    graph = Graph()
    banana = Node("banana")

    with pytest.raises(ValueError):
        nodes_list = graph.depth_first(banana)


def test_depth_first():
    graph = Graph()
    banana = graph.add_node('banana')
    apple = graph.add_node('apple')
    strawberry = graph.add_node('strawberry')
    tomato = graph.add_node('tomato')
    graph.add_edge(banana, apple)
    graph.add_edge(apple, strawberry)
    graph.add_edge(banana, tomato)
    nodes_list = graph.depth_first(banana)

    assert nodes_list == [banana.value, tomato.value, apple.value, strawberry.value]


def test_depth_first__node_not_in_graph():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = Node('d')
    graph.add_edge(a, b)
    graph.add_edge(b, c)

    with pytest.raises(ValueError):
        nodes_list = graph.depth_first(d)