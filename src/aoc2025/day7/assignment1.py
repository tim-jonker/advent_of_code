def process_file(file_path):
    result = 0
    with open(file_path) as f:
        beams = set()
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            if "S" in line:
                beams = {i for i, c in enumerate(line) if c == "S"}
                splitters = []
            else:
                splitters = [i for i, c in enumerate(line) if c == "^"]
            new_beams = set()
            for beam in beams:
                if beam in splitters:
                    result += 1
                    if beam - 1 >= 0:
                        new_beams.add(beam - 1)
                    if beam + 1 < len(line):
                        new_beams.add(beam + 1)
                else:
                    new_beams.add(beam)
            beams = new_beams

    return result


if __name__ == "__main__":
    result = process_file("input.txt")