import networkx as nx


def dfs(current_node, graph, num_paths, is_dac, is_fft):
    if current_node == 'dac':
        is_dac = True
    if current_node == 'fft':
        is_fft = True

    key = (current_node, is_dac, is_fft)

    if key in num_paths:
        return num_paths[key]

    values = 0
    for neighbour in graph.neighbors(current_node):
        if neighbour == 'out':
            if is_dac and is_fft:
                values += 1
            else:
                continue
        else:
            values += dfs(neighbour, graph, num_paths, is_dac, is_fft)

    num_paths[key] = values
    return values

def process_file(file_path):
    result = 0
    graph = nx.DiGraph()
    with open(file_path) as f:
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            input_line = line.split(": ")
            node = input_line[0]
            graph.add_node(node)
            for neighbor in input_line[1].split(" "):
                graph.add_edge(node, neighbor)

    result = dfs("svr", graph, {}, False, False)

    return result


if __name__ == "__main__":
    result = process_file("input.txt")