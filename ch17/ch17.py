import bz2
import re
import requests
from urllib.parse import unquote_to_bytes
import xmlrpc.client


def collect_cookie_value(requests_session, key):
    return requests_session.cookies.get_dict().get(key)


def traverse(regex, url, value='', cookie_key='info'):
    """Traverse the link chain while collecting cookie info."""
    cookie_data = ''
    session = requests.Session()
    response = session.get(url + value)
    cookie_data += collect_cookie_value(session, cookie_key)
    match = re.search(regex, response.text)

    while match is not None:
        value = match.group(1)  # Get the wanted value in the match
        response = session.get(url + value)
        cookie_data += collect_cookie_value(session, cookie_key)
        document = response.text
        print(document)
        match = re.search(regex, document)

    # Done, print the whole document for info and return the cookie info
    print(document)
    return cookie_data


def part1():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    regex = re.compile(r"and the next busynothing is (\d+)")

    cookie_data = traverse(regex, url, "12345")
    # cookie_data is a bzip2 encoded string
    # We gotta convert the plus signs to spaces for the bzip decompress to work
    data = unquote_to_bytes(cookie_data.replace('+', ' '))
    decompressed = bz2.decompress(data).decode()
    print(decompressed)


def part2():
    # We gotta call Mozart's father!
    phonebook_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    proxy = xmlrpc.client.ServerProxy(phonebook_url)
    print(proxy.phone('Leopold'))
    # We get 555-VIOLIN. We get to the following URL
    leopold_url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    # Send the message to Leopold inside a cookie! This was tricky
    response = requests.get(leopold_url, cookies={'info': 'the flowers are on their way'})
    print(response.text)
    # And we get the solution: balloons


def main():
    #  part1()
    part2()


if __name__ == "__main__":
    main()
