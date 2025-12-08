from math import prod

import numpy as np
from scipy.spatial import distance_matrix

class JunctionBox:
    id: int
    x: int
    y: int
    z: int

    def __init__(self, id, coords):
        self.id = id
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __repr__(self):
        return f"Junction({self.id}, {self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"Junction({self.id}, {self.x}, {self.y}, {self.z})"


def process_file(file_path, depth):
    result = 0
    with open(file_path) as f:
        positions = []
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            positions.append([int(c) for c in line.split(",")])

    positions = np.array(positions)
    dima = distance_matrix(positions, positions)
    junction_boxes = [JunctionBox(i, coords) for i, coords in enumerate(positions)]

    pairs = [(i, j) for i in junction_boxes for j in junction_boxes]
    distances = dima.flatten()

    long_form = [((i, j), d) for (i, j), d in zip(pairs, distances) if i < j]
    long_form.sort(key=lambda x: x[1])

    clusters = [set([box]) for box in junction_boxes]
    for (box1, box2), dist in long_form[:depth]:
        cluster1 = next(c for c in clusters if box1 in c)
        cluster2 = next(c for c in clusters if box2 in c)
        if cluster1 != cluster2:
            clusters.remove(cluster1)
            clusters.remove(cluster2)
            clusters.append(cluster1.union(cluster2))

    clusters.sort(key=lambda x: len(x), reverse=True)
    result = prod(len(c) for c in clusters[:3])

    return result


if __name__ == "__main__":
    result = process_file("input.txt", 1000)