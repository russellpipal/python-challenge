"""Challenge #1."""


def shift_char(char, amt):
    """Shift a character by number of characters indicated by amt."""
    ALPHABET_SIZE = 26
    amt = int(amt)
    if ord(char) < ord("a") or ord(char) > ord("z"):
        return char
    elif ord(char) + amt <= ord("z"):
        ch = ord(char) + amt
    else:
        ch = ord(char) + amt - ALPHABET_SIZE
    return chr(ch)


input_string = input("Enter a string: ")
input_amt = input("Enter an amount to shift: ")
output_string = ""
for ch in input_string:
    output_string += shift_char(ch, input_amt)
print(output_string)
