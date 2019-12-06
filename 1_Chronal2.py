import fileinput
from typing import List, Set


def main():
    changes: List[int] = []

    for line in fileinput.input():
        changes.append(int(line))

    freq: int = 0
    pastFreq: Set[int] = set()

    while True:
        for change in changes:
            freq += change
            if freq in pastFreq:
                print(freq)
                exit()
            pastFreq.add(freq)
            print(freq)


if __name__ == '__main__':
    main()
