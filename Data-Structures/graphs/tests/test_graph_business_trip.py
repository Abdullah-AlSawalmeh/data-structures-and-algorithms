# from challenges.graph_business_trip import *
# from graphs.graphs import *
# import pytest
# 
# def test_business_trip_1(return_graph):
#     expected = 82
#     actual = business_trip(return_graph,['Metroville','Pandora'])
#     assert actual == expected
# 
# def test_business_trip_2(return_graph):
#     expected = 115
#     actual = business_trip(return_graph,['Arendelle','Monstropolis','Naboo'])
#     assert actual == expected
# 
# def test_business_trip_3(return_graph):
#     actual = business_trip(return_graph,['Naboo','Pandora'])
#     assert not actual
# 
# def test_business_trip_4(return_graph):
#     actual = business_trip(return_graph,['Narnia','Arendelle','Naboo'])
#     assert not actual
# 
# @pytest.fixture
# def return_graph():
#     g = Graph()
#     node1 = g.add_node('Pandora')
#     node2 = g.add_node('Arendelle')
#     node3 = g.add_node('Metroville')
#     node4 = g.add_node('Monstropolis')
#     node5 = g.add_node('Narnia')
#     node6 = g.add_node('Naboo')
#     g.add_edge(node1, node2, 150)
#     g.add_edge(node1, node3, 82)
#     g.add_edge(node2, node3, 99)
#     g.add_edge(node2, node4, 42)
#     g.add_edge(node3, node4, 105)
#     g.add_edge(node3, node5, 37)
#     g.add_edge(node3, node6, 26)
#     g.add_edge(node4, node6, 73)
#     g.add_edge(node5, node6, 250)
#     return g