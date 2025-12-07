from collections import defaultdict

def process_file(file_path):
    with open(file_path) as f:
        beams = defaultdict(int)
        for i, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            if "S" in line:
                for i, c in enumerate(line):
                    if c == "S":
                        beams[i] += 1
                splitters = []
            else:
                splitters = [i for i, c in enumerate(line) if c == "^"]
            if splitters:
                new_beams = defaultdict(int)
                for beam, counts in beams.items():
                    if beam in splitters:
                        if beam - 1 >= 0:
                            new_beams[beam - 1] += counts
                        if beam + 1 < len(line):
                            new_beams[beam + 1] += counts
                    else:
                        new_beams[beam] += counts
                beams = new_beams

    return sum(beams.values())


if __name__ == "__main__":
    result = process_file("input.txt")