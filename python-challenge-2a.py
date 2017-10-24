"""Challenge 2a."""


def transform(input_str):
    ALPHABET_IN = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET_OUT = "cdefghijklmnopqrstuvwxyzab"
    return input_str.translate(str.maketrans(ALPHABET_IN, ALPHABET_OUT))


input_string = input("Enter a string: ")
print(transform(input_string))
