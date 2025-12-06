import numpy as np

def process_file(file_path):
    result = 0
    with open(file_path) as f:
        operators = []
        matrix = []
        for _, line in enumerate(f):
            if line[-1] == "\n":
                line = line[:-1]

            all_values = []
            current_value = ""
            for char in line:
                if current_value and char == " ":
                    all_values.append(int(current_value))
                    current_value = ""
                elif char == "*" or char == "+":
                    operators.append(char)
                elif char == " ":
                    continue
                else:
                    current_value += char
            if current_value != "":
                all_values.append(int(current_value))
            if all_values:
                matrix.append(all_values)

    matrix = np.array(matrix)
    matrix = matrix.T

    for operator, row in zip(operators, matrix):
        if operator == "*":
            result += np.prod(row)
        elif operator == "+":
            result += np.sum(row)

    return result


if __name__ == "__main__":
    result = process_file("input.txt")