def main():
    with open('evil2.gfx', 'rb') as f:
        data = f.read()

    # There are 5 different files interwined together
    # To get a file we have to pick a starting point and take steps of 5 bytes

    formats = ['jpg', 'png', 'gif', 'png', 'jpg']
    for i in range(5):
        extracted = data[i::5]
        with open(f'extracted{i}.{formats[i]}', 'wb') as f:
            f.write(extracted)


if __name__ == "__main__":
    main()
