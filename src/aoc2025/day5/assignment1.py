def process_file(file_path):
    reading_ranges = True
    result = 0
    fresh_ingredients = []
    with open(file_path) as f:
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            if line == "":
                reading_ranges = False
                continue

            if reading_ranges:
                fresh_range = line.split("-")
                fresh_ingredients.append((int(fresh_range[0]), int(fresh_range[-1])))
            else:
                for fresh_ingredient in fresh_ingredients:
                    if fresh_ingredient[0] <= int(line) <= fresh_ingredient[1]:
                        result += 1
                        break
    return result


if __name__ == "__main__":
    result = process_file("input.txt")