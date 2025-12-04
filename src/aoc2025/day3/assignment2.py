def process_file(file_path):
    result = 0
    with open(file_path) as f:
        for _, line in enumerate(f):
            digits = [int(char) for char in line.strip()]
            overall_index = -1
            for v in range(11,-1,-1):
                if v == 0:
                    sublist = digits[overall_index + 1:]
                else:
                    sublist = digits[overall_index + 1:-v]
                index = max(range(len(sublist)), key=sublist.__getitem__)
                overall_index += index + 1
                value = sublist[index]
                result += value * 10 ** v
    return result


if __name__ == "__main__":
    result = process_file("input.txt")