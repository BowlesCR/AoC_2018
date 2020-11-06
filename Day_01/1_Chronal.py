import fileinput


def main():
    freq: int = 0

    for line in fileinput.input():
        freq += int(line)

    print(freq)


if __name__ == "__main__":
    main()
