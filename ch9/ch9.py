from PIL import Image, ImageDraw


def load_sequence(filename):
    """Loads a sequence of comma-separated numbers from a file and returns it."""
    with open(filename) as f:
        data = []
        for line in f:
            data += [int(n) for n in line.strip(',\n').split(',')]
    return data


def connect_dots(sequence, size=500):
    """Connects the dots given as a single sequence of numbers, returning the resulting image.

    The sequence must have an even number of values, since the values will be taken by pairs
    by the line drawing function, representing coordinates.
    """
    image = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(image)
    draw.line(sequence)
    return image


def main():
    first = load_sequence('first.txt')
    second = load_sequence('second.txt')
    sequence = first + second
    print(sequence)
    image = connect_dots(sequence)
    image.show()


if __name__ == "__main__":
    main()
