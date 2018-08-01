from PIL import Image


def decode_image_message(filename):
    image = Image.open(filename)
    width, height = image.size

    values = []
    for x in range(0, width, 7):
        pixel = image.getpixel((x, height // 2))
        gray_level = pixel[0]
        values.append(gray_level)

    image.close()
    return "".join(chr(v) for v in values)


def main():
    print(decode_image_message("oxygen.png"))
    # Message:
    # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print("".join(chr(v) for v in next_level))


if __name__ == "__main__":
    main()
