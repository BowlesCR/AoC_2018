import fileinput


def main():
    print(sum([int(x) for x in fileinput.input()]))


if __name__ == "__main__":
    main()
