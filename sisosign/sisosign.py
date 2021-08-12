import random
import sys
from typing import List


def sisosign(people: List[str]) -> str:
    return random.choice(people)


def main() -> None:
    p = sisosign(sys.argv[1:])
    print(f"{p} should stay")


if __name__ == "__main__":
    main()
