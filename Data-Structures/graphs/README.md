# Graphs

Ih this project, we created a data structure called **Graph** in Python. We used three classes, _Node_, _Queue_, and _Graph_.

**Node** included the following:

    1. `value`.

**Queue** included the following:

    _Attributes_:
         1. `dq`.

    _methods_:
        * `enqueue`.
        * `dequeue`.


**Graph** included the following:

    _Attributes_:
         1. `adjacency_list`.


    _methods_:
        * `AddNode()`: Adds a new node to the graph, Takes in the value of that node, Returns the added node.
        * `AddEdge()`: Adds a new edge between two nodes in the graph, Include the ability to have a “weight”, Takes in the two nodes to be connected by the edge, Both nodes should already be in the Graph
        * `GetNodes()`: Returns all of the nodes in the graph as a collection (set, list, or similar)
        * `GetNeighbors()`: Returns a collection of edges connected to the given node, Takes in a given node, Include the weight of the connection in the returned collection
        * `Size()`: Returns the total number of nodes in the graph.
        * `isPathBFS`: Accepts two nodes as input and uses your traversal algorithm to determine if a path exists between the two nodes.


**User acceptance tests** are included with the following test cases:

*Graph* test cases:

    1. Can create a Graph.
    2. Can add a node.
    3. Can get size.
    4. Can add edge between two nodes.
    5. Can add multiple edges.
    6. Can get list of nodes in the graph with their weights.
    7. Can get list of neighbor-nodes of a specific nodes.
    8. Can return True is there is a path between two nodes.
    9. Can return False is there is no path between two nodes.