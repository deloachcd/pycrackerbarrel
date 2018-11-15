# pycrackerbarrel

## What the hell is this?
This repository hosts python code designed to provide an answer
to one of the greatest questions ever asked by humanity in our time
on Earth:

*"How many ways are there to solve that game on the table at Cracker Barrel?"*

## How the hell do I run this?
This program requires the popular `numpy` package to run, as the triangle
itself is represented internally as numpy's `array` type.

Once you are sure numpy is installed, open up your favorite command line
interface or graphical python (3.5+) interpreter, and run:

`python3 count_possible_sequences.py`

The main program takes around 15 minutes to execute on the developer's laptop,
though this time may vary based on the processing power available for the
program to utilize.

## How the hell do I know these numbers are correct?
Tests can be run on the primary unique component utilized in the main program,
the `CrackerBarrelTriangle` class, with Python's built-in `unittest` module.

Simply run:
`python3 -m unittest TestCrackerBarrelTriangle.py`
and you can run a set of unit tests on the code.
