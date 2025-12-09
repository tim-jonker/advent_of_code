import itertools


def process_file(file_path):
    result = 0
    with open(file_path) as f:
        positions = []
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            positions.append([int(c) for c in line.split(",")])

    result = max(abs(tile1[0] - tile2[0] + 1) * abs(tile1[1] - tile2[1] + 1) for tile1, tile2 in itertools.combinations(positions, 2))

    return result


if __name__ == "__main__":
    result = process_file("input.txt")