from tqdm import tqdm

def process_file(file_path):
    reading_ranges = True
    result = 0
    fresh_ingredients = []
    with open(file_path) as f:
        for _, line in tqdm(enumerate(f)):
            if line[-1] == "\n":
                line = line[:-1]
            if line == "":
                reading_ranges = False
                continue

            if reading_ranges:
                fresh_range = line.split("-")
                start_new, end_new = (int(fresh_range[0]), int(fresh_range[-1]))

                to_add = []

                for fresh_ingredient in fresh_ingredients:
                    start_existing, end_existing = fresh_ingredient
                    if start_existing < start_new and start_new <= end_existing:
                        # Eliminate left
                        start_new = end_existing + 1
                    elif start_existing >= start_new and end_existing <= end_new:
                        # Fully covered
                        new_left_part = (start_new, start_existing - 1)
                        to_add.append(new_left_part)
                        start_new = end_existing + 1
                    elif start_existing <= end_new and end_new < end_existing:
                        # Eliminate right
                        end_new = start_existing - 1
                        break

                    if start_new > end_new:
                        break

                to_add.append((start_new, end_new))
                for start, end in to_add:
                    if start <= end:
                        fresh_ingredients.append((start, end))
                fresh_ingredients = sorted(fresh_ingredients, key=lambda x: x[0])

            else:
                break

    for fresh_ingredient in fresh_ingredients:
        result += fresh_ingredient[1] - fresh_ingredient[0] + 1

    return result

if __name__ == "__main__":
    result = process_file("input.txt")