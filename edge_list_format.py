def read_edge_list(path_to_file, is_weighted=False):

    with open(path_to_file) as file:
        n_nodes, n_edges = [int(number) for number in file.readline().split(' ')]

        edges = []
        for _ in range(n_edges):
            if is_weighted:
                node1, node2, weight = [int(number) for number in file.readline().split(' ')]
                edges.append([node1, node2, weight])
            else:
                node1, node2 = [int(number) for number in file.readline().split(' ')]
                edges.append([node1, node2])

    return n_nodes, edges



