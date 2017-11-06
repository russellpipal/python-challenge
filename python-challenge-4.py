"""Python challenge #4."""

import urllib.request
import re


def scan_html(code):
    """Scan using for loop."""
    for i in range(400):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(code)
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")
            print(html)
            code = re.search(r'the next nothing is ([0-9]+)', html).group(1)
            print(code)


nothing = input("Enter a nothing: ")
scan_html(nothing)


# def scan_html(code, counter):
#     """Scan using recursion."""
#     if counter <= 400:
#         url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(code)
#         with urllib.request.urlopen(url) as response:
#             html = response.read().decode("utf-8")
#             print(html)
#             next_html = re.search(r'the next nothing is ([0-9]+)', html).group(1)
#             print(next_html)
#             counter += 1
#             scan_html(next_html, counter)

# nothing = input("Enter a nothing: ")
# scan_html(nothing, 0)
