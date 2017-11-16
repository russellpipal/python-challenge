"""Python Challenge #6."""

import re
import zipfile


first_code = "90052"
zf = zipfile.ZipFile("channel.zip")
message = ""


def read_file(file_name, comments):
    with zf.open(file_name + ".txt") as myfile:
        contents = myfile.read().decode("utf-8")
        try:
            next_code = re.search(r'nothing is ([0-9]+)', contents).group(1)
            info = zf.getinfo(file_name + ".txt")
            comments += info.comment.decode("utf-8")
            read_file(next_code, comments)
        except AttributeError:
            print(comments)


read_file(first_code, message)
