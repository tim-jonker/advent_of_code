def process_file(file_path):
    result = 0
    with open(file_path) as f:
        for _, line in enumerate(f):
            ranges = line.split(",")
            for my_range in ranges:
                start, end = map(int, my_range.split("-"))
                for value in range(start, end + 1):
                    result += process_value(value)
    return result


def process_value(value):
    value = str(value)
    if len(value) % 2 == 0:
        mid = len(value) // 2
        left = value[:mid]
        right = value[mid:]
        if left == right:
            return int(value)

    return 0


if __name__ == "__main__":
    result = process_file("/Users/tim.jonker/Documents/GitHub/advent_of_code/src/aoc2025/day2/input.txt")