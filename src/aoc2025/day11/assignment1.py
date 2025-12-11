import networkx as nx


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

    paths = nx.all_simple_paths(graph, source="you", target="out")
    result = len(list(paths))

    return result


if __name__ == "__main__":
    result = process_file("input.txt")