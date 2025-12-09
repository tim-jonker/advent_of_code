import itertools

import matplotlib.pyplot as plt

from shapely.geometry import polygon
from shapely.geometry import box
from tqdm import tqdm

def process_file(file_path):
    result = 0
    with open(file_path) as f:
        positions = []
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            positions.append([int(c) for c in line.split(",")])

    main_polygon = polygon.Polygon(positions)

    best_tile1 = None
    best_tile2 = None

    for tile1, tile2 in tqdm(itertools.combinations(positions, 2), total=122760):
        min_x = min(tile1[0], tile2[0])
        max_x = max(tile1[0], tile2[0])
        min_y = min(tile1[1], tile2[1])
        max_y = max(tile1[1], tile2[1])
        rect = box(min_x, min_y, max_x + 1, max_y + 1)
        area = (max_x + 1 - min_x) * (max_y + 1 - min_y)
        if area > result and main_polygon.covers(rect):
            best_tile1 = tile1
            best_tile2 = tile2
            result = area

    plt.figure(figsize=(5, 5))
    x, y = main_polygon.exterior.xy
    plt.plot(x, y, linewidth=2)  # outline
    plt.fill(x, y, alpha=0.3)  # optional fill

    min_x = min(best_tile1[0], best_tile2[0])
    max_x = max(best_tile1[0], best_tile2[0]) + 1
    min_y = min(best_tile1[1], best_tile2[1])
    max_y = max(best_tile1[1], best_tile2[1]) + 1
    rect = box(min_x, min_y, max_x, max_y)
    x, y = rect.exterior.xy
    plt.plot(x, y, linewidth=2)  # outline
    plt.fill(x, y, alpha=0.3, c="r")  # optional fill

    plt.axis('equal')
    plt.title("Shapely Polygon")
    plt.show()

    return result


if __name__ == "__main__":
    result = process_file("input.txt")