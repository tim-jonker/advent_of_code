def centered_windows(M, w):
    rows = len(M)
    cols = len(M[0])

    for i in range(rows):
        for j in range(cols):

            r0 = max(i - w, 0)
            r1 = min(i + w + 1, rows)
            c0 = max(j - w, 0)
            c1 = min(j + w + 1, cols)

            window = [row[c0:c1] for row in M[r0:r1]]

            yield (i, j, window)

def count_removable(grid):
    result = 0
    for i, j, win in centered_windows(grid, 1):
        if grid[i][j] == "@":
            surrounded_by = -1  # exclude self
            for row in win:
                for cell in row:
                    if cell == "@":
                        surrounded_by += 1
            if surrounded_by < 4:
                result += 1
    return result


def process_file(file_path):
    grid = []
    with open(file_path) as f:
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            grid.append(list(line))

    result = count_removable(grid)
    return result


if __name__ == "__main__":
    result = process_file("input.txt")