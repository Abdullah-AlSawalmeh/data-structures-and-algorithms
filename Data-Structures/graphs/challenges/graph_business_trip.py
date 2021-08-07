from graphs.graphs import *
# def business_trip(graph, cities):
#     """ return true if trip is possible with direct flights, and how much it would cost, otherwise return false. """
#     cost = 0
#     flag = True
# 
#     for i in range(len(cities)-1):
#         if not flag:
#             return False, '$0'
#         neighbors = graph.get_neighbors(cities[i])
#         for neighbor in neighbors:
#             if cities[i+1] == neighbor[0]:
#                 cost += neighbor[1]
#                 flag = True
#                 break
#             else:
#                 flag = False
#     if not flag :
#         cost = 0
#     return flag, '$'+str(cost)
# 
# if __name__ == "__main__":
#     graph = Graph()
#     Jordan = graph.add_node('Jordan')
#     Syria = graph.add_node('Syria')
#     KSA = graph.add_node('KSA')
#     Iraq = graph.add_node('Iraq')
#     Turkey = graph.add_node('Turkey')
#     graph.add_edge(Jordan, Iraq,30)
#     graph.add_edge(Iraq, Jordan,30)
#     graph.add_edge(Jordan, Syria,20)
#     graph.add_edge(Syria, Jordan,20)
#     graph.add_edge(Jordan, KSA,35)
#     graph.add_edge(KSA, Jordan,35)
#     graph.add_edge(Syria, Turkey,40)
#     graph.add_edge(Turkey, Syria,40)
#     graph.add_edge(Turkey, Iraq,35)
#     graph.add_edge(Iraq, Turkey,35)
#     graph.add_edge(Iraq, Syria,25)
#     graph.add_edge(Syria, Iraq,25)
#     graph.add_edge(KSA, Iraq,40)
#     graph.add_edge(Iraq, KSA,40)
#     cities_lists =[[Jordan, Syria, Turkey],[Turkey,KSA,Jordan],[Iraq, Syria],[KSA,Turkey]]
# 
#     business_trip(graph, cities_lists)

def business_trip(graph, city_arr):
    node_list = graph.get_nodes()
    node_dict = {}
    weight = 0
    for node in node_list:
        node_dict[node.value] = node
    for index in range(len(city_arr) - 1):
        first_city = city_arr[index]
        second_city = city_arr[index + 1]
        first_node = node_dict[first_city]
        second_node = node_dict[second_city]
        first_city_neighbors = graph.get_neighbors(first_node)
        linked = False
        for edge in first_city_neighbors:
            if edge[0] == second_node:
                weight += edge[1]
                linked = True
        if not linked:
            return None
    return weight

if __name__ == "__main__":
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstropolis')
    node5 = g.add_node('Narnia')
    node6 = g.add_node('Naboo')
    g.add_edge(node1, node2, 150)
    g.add_edge(node1, node3, 82)
    g.add_edge(node2, node3, 99)
    g.add_edge(node2, node4, 42)
    g.add_edge(node3, node4, 105)
    g.add_edge(node3, node5, 37)
    g.add_edge(node3, node6, 26)
    g.add_edge(node4, node6, 73)
    g.add_edge(node5, node6, 250)
    print(business_trip(g,['Metroville','Pandora']))
    print('new---------------------------------')
    print(business_trip(g,['Arendelle','Monstropolis','Naboo']))
    print('new---------------------------------')
    print(business_trip(g,['Naboo','Pandora']))
    print('new---------------------------------')
    print(business_trip(g,['Narnia','Arendelle','Naboo']))