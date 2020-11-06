import fileinput
from itertools import combinations


def main():

    combo: tuple[str, str]
    for combo in combinations([x.rstrip() for x in fileinput.input()], 2):

        diffs: int = 0
        ch1: str
        ch2: str
        for ch1, ch2 in zip(combo[0], combo[1]):
            if ch1 != ch2:
                diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            output: str = ""
            for ch1, ch2 in zip(combo[0], combo[1]):
                if ch1 == ch2:
                    output += ch1
            print(output)


if __name__ == "__main__":
    main()
