import random
from typing import List

import click


@click.command()
@click.argument("people", nargs=-1)
def sisosign(people: List[str]) -> None:
    """Can't decide who should stay on the story?
    Why not have a computer make these tough choices for you?

    PEOPLE is a list of one or more names. Only one will be chosen to stay.
    """
    if len(people) < 1:
        print("Please provide at least one name or use the --help option.")
        exit(1)
    p = random.choice(people)
    print(f"{p} should stay")


if __name__ == "__main__":
    sisosign()
