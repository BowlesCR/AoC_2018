import fileinput
from typing import Dict


def main():
    doubles: int = 0
    triples: int = 0

    for line in fileinput.input():
        letters: Dict[str, int] = {}
        for letter in line:
            if letter in letters:
                letters.update({letter: letters[letter] + 1})
            else:
                letters.update({letter: 1})

        if 2 in letters.values():
            doubles += 1

        if 3 in letters.values():
            triples += 1

    print(doubles * triples)


if __name__ == "__main__":
    main()
