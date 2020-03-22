#!/usr/bin/env python3

import click

from mkp import __title__, __version__
from mkp.algorithm import GreedyAlgorithm
from mkp.utils.parser import Parser


@click.command()

# -h, --help
@click.help_option("-h", "--help")

# --version
@click.version_option(
    version=__version__,
    prog_name=__title__,
    message="You are using version %(version)s of %(prog)s",
)

# -k, --knapsacks
@click.option(
    "-k",
    "--knapsacks",
    "knapsacks",
    required=True,
    type=int,
    help="The total number of knapsacks to fill",
)

# -s, --size
@click.option(
    "-s",
    "--size",
    "knapsack_size",
    required=True,
    type=int,
    help="The size of each knapsack",
)

# -f, --file
@click.option(
    "-f",
    "--file",
    required=True,
    type=click.Path(),
    nargs=1,
    default=None,
    help="Path to objects for knapsacking",
)
def main(**kwargs):
    print(kwargs)

    parser = Parser(kwargs["file"])

    # try:
    objects = parser.objects
    avg_value = parser.avg_value

    objects.sort(key=lambda x: x.value, reverse=True)
    # (len(players) // kwargs)
    # players: list, knapsacks: int, team_size: int, average_value
    teams = GreedyAlgorithm(
        objects,
        kwargs["knapsacks"],
        kwargs["knapsack_size"],
        avg_value * kwargs["knapsack_size"],
    ).teams
    # except Exception as e:
    #     print(f'Error: {e}')

    print(teams)


if __name__ == "__main__":
    main()
