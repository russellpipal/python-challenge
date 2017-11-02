"""Challenge #2."""

import re

mess = open("challenge-2-mess.txt")
cont = mess.read()
print(re.findall(r'[a-zA-Z0-9]', cont))
mess.close()
