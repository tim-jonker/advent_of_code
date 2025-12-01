def process_file(file_path):
    idx = 50
    pad = list(range(100))
    result = 0
    with open(file_path) as f:
        for _, line in enumerate(f):
            line = line.replace("\n", "")
            direction = line[0]
            value = int(line[1:])

            whole_turns = value // len(pad)
            value %= len(pad)

            if direction == "L":
                if idx > 0 >= idx - value:
                    result += 1
                idx = (idx - value) % len(pad)
            elif direction == "R":
                if idx + value >= len(pad):
                    result += 1
                idx = (idx + value) % len(pad)
            result += whole_turns

    return result

if __name__ == "__main__":
    result = process_file("input1.txt")