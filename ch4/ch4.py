import re
import requests


def traverse(regex, url, value=''):
    document = requests.get(url + value).text
    match = re.search(regex, document)

    while match is not None:
        value = match.group(1)  # Get the wanted value in the match
        document = requests.get(url + value).text
        match = re.search(regex, document)
        print(value)

    # Done, print the whole document for info
    print(document)


def main():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    regex = re.compile(r"and the next nothing is (\d+)")

    # Starting value
    #  traverse(regex, url, "12345")

    # Second part
    traverse(regex, url, "8022")


if __name__ == "__main__":
    main()
