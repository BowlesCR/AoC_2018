import fileinput


def main():
    fab: list[list[int]] = [[0] * 1000 for _ in range(1000)]
    line: str
    for line in fileinput.input():
        tokens = line.rstrip().split(" ")
        offset = [int(_) for _ in tokens[2].strip(":").split(",")]
        dims = [int(_) for _ in tokens[3].split("x")]

        for x in range(offset[0], offset[0] + dims[0]):
            for y in range(offset[1], offset[1] + dims[1]):
                fab[x][y] += 1

    overlaps = 0
    for row in fab:
        overlaps += len([x for x in row if x > 1])

    print(overlaps)


if __name__ == "__main__":
    main()
