# mkp
The multidimensional 0–1 knapsack problem solved using a greedy algorithm.

## About

This tool was born from nessecity and can be used to determine any combination of balanced knapsacks based on an object's value.

## Problem Statement

*note: Although the following is not the only use for this tool, this was the original use case.*

You are holding a Beer Olympics, the goal is to create teams that are equally matched(or as close as possible) to ensure each team has a fair chance. Each player has a rating for each event, the ratings add up to the player's overall value. Implement a greedy algorithm to solve the multidimensional 0–1 knapsack problem.

Details:

* Each team has 3 players
* there are 5 teams
* Each player has a total value that is calculated by the given file inputs

### File input:

Below are the details about each player. The rating for each player is separated by a semi-colon, all ratings should be summed to find a player's value.

```
-- Name; Case Race; Beer Ball; Flip 50;
Nicole;1;2;2;
Jenna;2;2;5;
Krendan;4;3;3;
Dylan;4;3;3;
Luke;5;5;3;
Jason;5;4;3;
Brendan;5;4;3;
James E;3;3;3;
Aidan;3;4;5;
Daniel;4;5;4;
Maya;3;3;5;
James C;3;3;3;
Kayvan;3;2;2;
Steph;3;2;4;
Kevin;3;3;3;
```

## Installation

For installation just run the make target

`make`

## Usage

### CLI

```
mkp -h
Usage: __main__.py [OPTIONS]

Options:
  -h, --help               Show this message and exit.
  --version                Show the version and exit.
  -e, --examples           Generate example files
  -k, --knapsacks INTEGER  The total number of knapsacks to fill  [required]
  -c, --capacity INTEGER   The capacity of each knapsack  [required]
  -f, --file PATH          Path to objects for knapsacking  [required]
```

### Input

the object input is provided via a file, the format for which is defined below.

*Comment Deliminator: `--`* 

```
-- Object Title; Event 1 Rating; Event 2 Rating; ... Event N Rating;
```

## Development

To get all necessary dependencies run:

```
make init
```

Then enter a new pipenv shell via:

```
pipenv shell
```

Now to run the cli from source run

```
python3 -m mkp
```


