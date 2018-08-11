def evolve(s):
    """Perform run-length encoding of the given string, generating a new string."""
    result = ""
    i = 0
    while i < len(s):
        current = s[i]
        count = 0
        while i < len(s) and s[i] == current:
            count += 1
            i += 1
        result += str(count) + current
    return result


def main():
    seq = "1"
    for step in range(30):
        seq = evolve(seq)
    print(len(seq))


if __name__ == "__main__":
    main()
