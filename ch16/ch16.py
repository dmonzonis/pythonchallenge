from PIL import Image


def find_pink_strip(img, y):
    """Find the position of the pink strip at the given y value.

    Return the position of the pixel prior to the first pink pixel in the 5-pixel wide
    pink strip in the RGB image at the given y value.
    """
    width, height = img.size
    assert(y < height)
    consecutive = 0
    for x in range(width):
        color = img.getpixel((x, y))
        if color == (255, 0, 255):  # If color is pink
            consecutive += 1
            # Check if we've completed the 5-pixel strip
            if consecutive == 5:
                # Strip found, return position to the pixel before it (which should be white)
                return x - consecutive
        else:
            consecutive = 0
    return None


def draw_shifted_line(img, orig, y, shift):
    """Draw the line at height y from the original but shifted to the left by a certain value."""
    assert(img.size == orig.size)
    width = orig.size[0]
    for x in range(width):
        img.putpixel((x, y), orig.getpixel(((x + shift) % width, y)))
    return img


def align_horizontal_strips(img):
    """Draws an image resulting of aligning all the pink strips vertically on the left."""
    height = img.size[1]
    aligned_img = Image.new(img.mode, img.size)
    for y in range(height):
        # Find pink strip location and redraw every line using those locations
        strip_pos = find_pink_strip(img, y)
        draw_shifted_line(aligned_img, img, y, strip_pos)
    return aligned_img


def main():
    mozart = Image.open("mozart.gif").convert('RGB')
    aligned_mozart = align_horizontal_strips(mozart)
    aligned_mozart.show()


if __name__ == "__main__":
    main()
