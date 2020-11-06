import fileinput
from typing import List


def main():
    boxes: List[str] = []
    for line in fileinput.input():
        for box in boxes:
            diffs: int = 0
            for ch1, ch2 in zip(line.rstrip(), box):
                if ch1 != ch2:
                    diffs += 1
            if diffs == 1:
                output: str = ''
                for ch1, ch2 in zip(line.rstrip(), box):
                    if ch1 == ch2:
                        output += ch1
                print(output)

        boxes.append(line.rstrip())


if __name__ == '__main__':
    main()
