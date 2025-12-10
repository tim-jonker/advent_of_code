import re
from copy import deepcopy
import pulp

from tqdm import tqdm

def linprog(buttons, d):
    num_buttons = len(buttons)
    n = len(d)

    # Create optimization problem
    prob = pulp.LpProblem("Button_Sequence", pulp.LpMinimize)

    # Decision variables: number of times each button is pressed
    x = [pulp.LpVariable(f"x_{k}", lowBound=0, cat="Integer")
         for k in range(num_buttons)]

    # Objective: minimize total presses
    prob += pulp.lpSum(x[k] for k in range(num_buttons))

    # Constraints: match the desired vector
    for i in range(n):
        prob += pulp.lpSum(buttons[k][i] * x[k] for k in range(num_buttons)) == d[i]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=1))
    return sum([x[k].value() for k in range(num_buttons)])


def process_file(file_path):
    result = 0
    with open(file_path) as f:
        for _, line in tqdm(enumerate(f), total=198):
            if line[-1] == "\n":
                line = line[:-1]
            desired_pattern = tuple([int(char) for char in re.findall(r'\{(.*?)\}', line)[0].split(",")])
            buttons = [[int(button) for button in button_sequence.split(",")] for button_sequence in re.findall(r'\((.*?)\)', line) ]

            button_vecs = []
            for button in buttons:
                button_vec = [0] * len(desired_pattern)
                for pos in button:
                    button_vec[pos] += 1
                button_vecs.append(button_vec)

            result += linprog(button_vecs, desired_pattern)

    return result


def find_buttons_pressed(buttons, desired_pattern):
    current_sequences = {tuple([0] * len(desired_pattern)): 0}
    while True:
        new_sequences = {}
        for current_sequence, buttons_pressed in current_sequences.items():
            for button in buttons:
                new_sequence = list(deepcopy(current_sequence))
                for pos in button:
                    new_sequence[pos] += 1
                new_sequence = tuple(new_sequence)
                if new_sequence not in current_sequences and not any(val > desired for val, desired in zip(new_sequence, desired_pattern)):
                    new_sequences[tuple(new_sequence)] = buttons_pressed + 1
                if new_sequence == desired_pattern:
                    return buttons_pressed + 1
        current_sequences = new_sequences


if __name__ == "__main__":
    result = process_file("input.txt")