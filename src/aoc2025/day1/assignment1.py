def process_file(file_path):
    idx = 50
    pad = list(range(100))
    result = 0
    with open(file_path) as f:
        for _, line in enumerate(f):
            line = line.replace("\n", "")
            direction = line[0]
            value = int(line[1:])

            if direction == "L":
                idx = (idx - value) % len(pad)
            elif direction == "R":
                idx = (idx + value) % len(pad)

            if idx == 0:
                result += 1

    return result

if __name__ == "__main__":
    result = process_file("input1.txt")