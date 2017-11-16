"""Python Challenge #7."""

from PIL import Image

im = Image.open("oxygen.png")
width, height = im.size
box = (0, int(height / 2), width, int(height / 2 + 1))
line = im.crop(box)
pixel_values = list(line.getdata())
message = ""
for pixel in range(len(pixel_values) - 1):
    # this eliminates the duplicates
    if pixel_values[pixel][0] != pixel_values[pixel + 1][0]:
        message += chr(pixel_values[pixel][0])
print(message)

# but the duplicate 1's have to be added back here
codes = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for code in codes:
    print(chr(code))
