#!/usr/bin/env python3

import sys

import click

from mkp import __title__, __version__
from mkp.algorithm import GreedyAlgorithm
from mkp.utils.parser import Parser
from mkp.utils.example import players


def createExample(ctx: click.Context, param: click.Parameter, value):
    if not value or ctx.resilient_parsing:
        return
    try:
        click.echo("writing example data...")
        file = open("./players.txt", "w+")
        file.writelines(players.lstrip())
        file.close()
        click.echo("done.\n")
        click.echo(
            "To run the example, pass in the following parameters to the cli:\n-f ./players.txt\n-k 5\n-c 3"
        )

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        ctx.exit()


@click.command()

# -h, --help
@click.help_option("-h", "--help")

# --version
@click.version_option(
    version=__version__,
    prog_name=__title__,
    message="You are using version %(version)s of %(prog)s",
)

# -e, --examples
@click.option(
    "-e",
    "--examples",
    required=False,
    is_flag=True,
    expose_value=False,
    is_eager=True,
    callback=createExample,
    default=False,
    help="Generate example files",
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

# -c, --capacity
@click.option(
    "-c",
    "--capacity",
    "knapsack_capacity",
    required=True,
    type=int,
    help="The capacity of each knapsack",
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
    # parse the data
    parser = Parser(kwargs["file"])

    try:
        objects = parser.objects
        avg_value = parser.avg_value

        # Check if the users put in valid values
        if (len(objects) // kwargs["knapsacks"]) != kwargs["knapsack_capacity"]:
            click.echo(
                "Error: the number of objects does not match the given number of knapsacks and capacity of each knapsack"
            )
            sys.exit(1)

        objects.sort(key=lambda x: x.value, reverse=True)
        knapsacks = GreedyAlgorithm(
            objects,
            kwargs["knapsacks"],
            kwargs["knapsack_capacity"],
            avg_value * kwargs["knapsack_capacity"],
        ).knapsacks
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        for i, knapsack in enumerate(knapsacks):
            print(f"Knapsack {i+1}: {knapsack}")


if __name__ == "__main__":
    main()
