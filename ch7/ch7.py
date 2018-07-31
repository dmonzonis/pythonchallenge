import re
import zipfile


def traverse(value, zip_file):
    values = [value]
    while True:
        with zip_file.open(value + ".txt") as next_file:
            regex = re.compile(r"Next nothing is (\d+)")
            data = next_file.read()
            decoded_text = data.decode("utf-8")
            match = re.match(regex, decoded_text)
            if match is None:
                break
            value = match.group(1)
            values.append(value)

    # Done, print the whole document
    print(decoded_text)
    # Return the list of ordered values encountered
    return values


def collect_comments(values, zip_file):
    comments = []
    for value in values:
        comment = zip_file.getinfo(value + ".txt").comment.decode("utf-8")
        comments.append(comment)

    return "".join(c for c in comments)


with zipfile.ZipFile("channel.zip") as channel:
    initial_value = "90052"
    values = traverse(initial_value, channel)
    # Collect the comments
    message = collect_comments(values, channel)
    print(message)
