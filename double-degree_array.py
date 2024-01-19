from edge_list_format import read_edge_list
from degree_array import count_degrees

def double_degrees(n_nodes, edges):

    # find neighbours
    neighbours_list = []
    for v in range(1, n_nodes + 1):

        neighbours = []
        for pair in edges:
            if v in pair:
                neighbour = pair[(pair.index(v) + 1) % 2]
                neighbours.append(neighbour)

        # avoid double countings
        neighbours_list.append(list(set(neighbours)))

    # count degree of neighbours and sum them
    double_degrees = []
    double_deg = 0

    degrees = count_degrees(n_nodes, edges)
    for neighbours in neighbours_list:
        neighbours_degrees = [degrees[v-1] for v in neighbours]
        double_degrees.append(sum(neighbours_degrees))

    return double_degrees

n_nodes, edges = read_edge_list('/home/fabio/PycharmProjects/Rosalind/datasets/rosalind_ddeg.txt')
# print(*double_degrees(n_nodes, edges))