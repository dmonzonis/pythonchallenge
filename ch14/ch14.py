from math import sqrt
from PIL import Image


def turn_right(direction):
    return (-direction[1], direction[0])


def take_step(position, direction):
    return tuple(sum(i) for i in zip(position, direction))


def roll_up_image(original):
    assert(original.size == (10000, 1))  # Only size supported by the operation
    new_size = int(sqrt(original.size[0]))  # 10000x1 image will be rolled up into a 100x100 one
    result = Image.new(original.mode, (new_size, new_size))

    visited = [[False for _ in range(100)] for _ in range(100)]
    pos = (0, 0)  # Position on the new image
    direction = (1, 0)
    # To draw the spiral, go straight whenever we can, and if we can't, turn right
    for i in range(10000):
        # Draw the pixel
        result.putpixel(pos, original.getpixel((i, 0)))
        visited[pos[1]][pos[0]] = True
        # Move one step further and check if we've visited it already or we're at the limits
        new_pos = take_step(pos, direction)
        if any([val == 100 for val in new_pos]) or visited[new_pos[1]][new_pos[0]]:
            # Turn right
            direction = turn_right(direction)
            pos = take_step(pos, direction)
        else:
            # Keep going forward
            pos = new_pos

    return result


def main():
    wire = Image.open("wire.png")
    spiral = roll_up_image(wire)
    spiral.show()


if __name__ == "__main__":
    main()
