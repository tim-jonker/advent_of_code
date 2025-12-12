from black.trans import defaultdict
from ortools.sat.python import cp_model
from shapely.ops import unary_union
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.plotting import plot_polygon  # Shapely 2.0
from tqdm import tqdm


def shape_to_polygon(coords):
    """Convert set of (x,y) cells into a merged Shapely polygon."""
    cells = []
    for x, y in coords:
        # Square cell from (x,y) to (x+1, y+1)
        cell = Polygon([(x, y), (x+1, y), (x+1, y+1), (x, y+1)])
        cells.append(cell)
    return unary_union(cells)

def plot_shape(poly):
    fig, ax = plt.subplots()
    plot_polygon(poly, ax=ax, add_points=False)
    ax.set_aspect("equal")
    plt.gca().invert_yaxis()  # Optional: match ASCII orientation
    plt.show()

def parse_shape(ascii_shape):
    """
    ascii_shape: multi-line string
    Returns: set of (x, y) coordinates where '#' occurs.
    """
    coords = set()
    lines = ascii_shape.strip().splitlines()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                coords.add((x, y))

    return coords

def rotate90(shape):
    return {(y, -x) for (x, y) in shape}

def flip_horizontal(shape):
    return {(-x, y) for (x, y) in shape}

def normalize(shape):
    """Move shape so min x,y = 0 for comparison."""
    minx = min(x for x, y in shape)
    miny = min(y for x, y in shape)
    return {(x-minx, y-miny) for (x, y) in shape}

def all_transformations(shape):
    shapes = set()
    s = normalize(shape)
    for _ in range(4):
        shapes.add(tuple(sorted(s)))
        s = normalize(rotate90(s))
    # flip and rotate again
    s = normalize(flip_horizontal(normalize(shape)))
    for _ in range(4):
        shapes.add(tuple(sorted(s)))
        s = normalize(rotate90(s))
    # convert back to sets
    return [set(coords) for coords in shapes]

def placements(grid, shape):
    rows, cols = len(grid), len(grid[0])
    result = []

    for orient in all_transformations(shape):
        # bounding box
        maxx = max(x for x,y in orient)
        maxy = max(y for x,y in orient)

        for oy in range(rows - maxy):
            for ox in range(cols - maxx):
                coords = {(ox + x, oy + y) for (x, y) in orient}
                if all(grid[y][x] == 0 for x, y in coords):
                    result.append(coords)

    return result

def solve(grid, shapes):
    if sum(len(shape) for shape in shapes) > len(grid) * len(grid[0]):
        return False
    else:
        return True
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    vars = {}
    covers = {(x, y): [] for y in range(len(grid)) for x in range(len(grid[0]))}
    for shape_idx, shape in enumerate(shapes):
        vars[shape_idx] = {}
        placement_vars = []
        for placement_idx, placement in enumerate(placements(grid, shape)):
            var = model.NewBoolVar(f"place_{shape_idx}_{placement_idx}")
            vars[shape_idx][placement_idx] = var
            placement_vars.append(var)
            for x, y in placement:
                covers[(x, y)].append(var)

        model.add(sum(placement_vars) == 1)
    for (x, y), cover_vars in covers.items():
        model.add(sum(cover_vars) <= 1)
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        return True

def process_file(file_path):
    result = 0
    raw = open("input.txt").read()
    all_shapes = [normalize(parse_shape(part.split("\n", 1)[1])) for part in raw.strip().split("\n\n")[:-1]]

    for problem in tqdm(raw.strip().split("\n\n")[-1].split("\n")):
        grid_size = problem.split(": ")[0].split("x")
        width = int(grid_size[0])
        length = int(grid_size[1])
        grid = [[0] * width] * length
        shape_ids = [int(id) for id in problem.split(": ")[1].split(" ")]
        shapes = [all_shapes[idx] for idx, num in enumerate(shape_ids) for _ in range(num)]

        if solve(grid, shapes):
            result += 1
    return result


if __name__ == "__main__":
    # print(
    #     sum(
    #         [
    #             (int(line.split("x")[0]) * int(line.split(":")[0].split("x")[1])) >= 9 * sum(list(map(int, line.split()[1:])))
    #             for line in open("input.txt").read().split("\n\n")[-1].split("\n")
    #         ]
    #     )
    # )
    result = process_file("input.txt")