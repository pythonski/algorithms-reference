from edge_list_format import read_edge_list
def count_degrees(n_nodes, edges):

    # flatten list of edges to get vertices with repetitions
    V = [item for sublist in edges for item in sublist]

    # count instances of each vertex
    degs = []
    for v in range(1, n_nodes + 1):
        deg = V.count(v)
        degs.append(deg)

    return degs
