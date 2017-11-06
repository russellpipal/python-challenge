"""Python Challenge #5."""

import pickle


def print_line(code):
    """Inputs a list of tuples (m,n), and prints the character m, n times."""
    line = ""
    for item in range(len(code)):
        instruction = code[item]
        line += instruction[0] * instruction[1]
    print(line)


with open('banner.p', 'rb') as f:
    data = pickle.load(f)
    for i in range(len(data)):
        print_line(data[i])
