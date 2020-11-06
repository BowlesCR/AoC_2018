import fileinput
import re


class Claim:
    def __init__(self, _id: str, offset: tuple[int, int], dims: tuple[int, int]):
        self.id = _id
        self.offset = offset
        self.dims = dims


def main():
    claims: list[Claim] = []
    for line in fileinput.input():

        match = re.match(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)", line)
        g = match.groups()
        claims.append(
            Claim(_id=g[0], offset=(int(g[1]), int(g[2])), dims=(int(g[3]), int(g[4])))
        )

    fab: list[list[int]] = [[0] * 1000 for _ in range(1000)]

    for c in claims:

        for x in range(c.offset[0], c.offset[0] + c.dims[0]):
            for y in range(c.offset[1], c.offset[1] + c.dims[1]):
                fab[x][y] += 1

    overlaps = 0
    for row in fab:
        overlaps += len([x for x in row if x > 1])

    for c in claims:
        overlap = False
        for x in range(c.offset[0], c.offset[0] + c.dims[0]):
            if any([_ > 1 for _ in fab[x][c.offset[1] : c.offset[1] + c.dims[1]]]):
                overlap = True
                break
        if not overlap:
            print(c.id)
            break


if __name__ == "__main__":
    main()
