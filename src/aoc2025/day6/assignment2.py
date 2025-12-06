import numpy as np
import pandas as pd

def process_file(file_path):
    result = 0
    with open(file_path) as f:

        matrix = []
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]
            matrix.append([c for c in line])

    matrix = np.array(matrix)
    matrix = matrix.T
    df = pd.DataFrame(matrix)
    operators = []
    all_problems = []
    problem = []
    for row in matrix:
        number = ""
        for value in row:
            if value in ["*", "+"]:
                operators.append(value)
            elif value == " ":
                continue
            else:
                number += value
        if number != "":
            number = int(number)
            problem.append(number)
        else:
            all_problems.append(problem)
            problem = []
    all_problems.append(problem)

    for operator, row in zip(operators, all_problems):
        if operator == "*":
            result += np.prod(row)
        elif operator == "+":
            result += np.sum(row)

    return result


if __name__ == "__main__":
    result = process_file("input.txt")