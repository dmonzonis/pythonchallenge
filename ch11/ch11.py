from PIL import Image


def separate_image(img):
    """Separates the even-valued and odd-valued pixels from an image, returning 2 images."""
    width, height = img.size
    odd = Image.new('RGB', img.size)
    even = Image.new('RGB', img.size)

    for x in range(width):
        for y in range(height):
            color = img.getpixel((x, y))
            # Consider a pixel "even" if the sum of its coordinates is even
            if (x + y) % 2 == 0:
                even.putpixel((x, y), color)
            else:
                odd.putpixel((x, y), color)

    return odd, even


def main():
    img = Image.open('cave.jpg')
    odd, even = separate_image(img)
    odd.show()
    even.show()


if __name__ == "__main__":
    main()
