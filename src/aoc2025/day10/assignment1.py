import re
from copy import deepcopy


def process_file(file_path):
    result = 0
    with open(file_path) as f:
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            desired_pattern = tuple([char == "#" for char in re.findall(r'\[(.*?)\]', line)[0]])
            buttons = [[int(button) for button in button_sequence.split(",")] for button_sequence in re.findall(r'\((.*?)\)', line) ]

            result += find_buttons_pressed(buttons, desired_pattern)

    return result


def find_buttons_pressed(buttons, desired_pattern):
    current_sequences = {tuple([False] * len(desired_pattern)): 0}
    while True:
        new_sequences = {}
        for current_sequence, buttons_pressed in current_sequences.items():
            for button in buttons:
                new_sequence = list(deepcopy(current_sequence))
                for pos in button:
                    new_sequence[pos] = not new_sequence[pos]
                new_sequence = tuple(new_sequence)
                if new_sequence not in current_sequences:
                    new_sequences[tuple(new_sequence)] = buttons_pressed + 1
                if new_sequence == desired_pattern:
                    return buttons_pressed + 1
        current_sequences = new_sequences


if __name__ == "__main__":
    result = process_file("input.txt")