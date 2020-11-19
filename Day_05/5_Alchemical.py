import fileinput
from collections import deque


def main():

    line: deque[str] = deque(fileinput.input()[0].rstrip())

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

    print(len(newline))


if __name__ == "__main__":
    main()
