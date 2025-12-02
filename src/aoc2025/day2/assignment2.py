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

def split_every_x(s, x):
    return [int(s[i:i+x]) for i in range(0, len(s), x)]

def process_value(value):
    value = str(value)
    for i in range(1, len(value) + 1):
        if len(value) % i == 0:
            substrings = split_every_x(value, i)
            if len(substrings) > 1 and len(set(substrings)) == 1:
                return int(value)

    return 0


if __name__ == "__main__":
    result = process_file("/Users/tim.jonker/Documents/GitHub/advent_of_code/src/aoc2025/day2/input.txt")