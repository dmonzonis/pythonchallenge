import re
import requests

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="


def traverse(value):
    document = requests.get(URL + value).text
    regex = re.compile(r"and the next nothing is (\d+)")
    match = re.search(regex, document)

    while match is not None:
        value = match.group(1)  # Get the number in the match
        document = requests.get(URL + value).text
        match = re.search(regex, document)
        print(value)

    # Done, print the whole document for info
    print(document)


# Starting value
#  traverse("12345")

# Second part
traverse("8022")
