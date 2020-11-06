import fileinput
from collections import Counter


def main():
    doubles: int = 0
    triples: int = 0

    for line in fileinput.input():
        counter = Counter(line.rstrip())

        if 2 in [x[1] for x in counter.most_common()]:
            doubles += 1
        if 3 in [x[1] for x in counter.most_common()]:
            triples += 1

    print(doubles * triples)


if __name__ == "__main__":
    main()
