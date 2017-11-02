"""Python Challenge #3"""

import re

cont = open("challenge-3-text.txt").read()
print(re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', cont))

# Works! Get all of the small letters and put them together.
