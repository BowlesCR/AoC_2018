import fileinput
from collections import deque


def main():

    fi: str = fileinput.input()[0].rstrip()
    units: set[str] = set(fi.lower())

    sizes: list[int] = []

    for unit in units:

        line: deque[str] = deque(fi.replace(unit, '').replace(unit.swapcase(), ''))

        newline: deque[str] = deque()

        while line:
            y: str = line.popleft()
            if newline:
                x: str = newline.pop()
                if x.swapcase() != y:
                    newline.append(x)
                    newline.append(y)
            else:
                newline.append(y)

        sizes.append(len(newline))

    print(min(sizes))


if __name__ == "__main__":
    main()
