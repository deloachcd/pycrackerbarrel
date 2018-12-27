# pycrackerbarrel

![cracker barrel boys](https://github.com/deloachcd/pycrackerbarrel/blob/master/images/cracker_barrel_boys.png?raw=tru://raw.githubusercontent.com/deloachcd/pycrackerbarrel/master/images/cracker_barrel_boys.png)

## What is this?
This repository hosts python code written to provide an answer
to one of the greatest questions humanity has ever asked:

*"How many ways are there to solve that game on the table at Cracker Barrel?"*

## How do I run this?
The primary component of this program requires the popular `numpy` package to
run, so make sure that's installed.

If you don't have it, you can easily install it via `pip`,
typically in a fashion like this:
`python3 -m pip install numpy`

Once you are sure numpy is installed, open up your favorite command line
interface or graphical python (3.5+) interpreter, and run:

`python3 count_possible_sequences.py`

The main program takes around 15 minutes to execute on the developer's laptop,
though this time may vary based on the processing power available for the
program to utilize.

## How do I know these numbers are correct?
Tests can be run on the primary unique component utilized in the main program,
the `CrackerBarrelTriangle` class, with Python's built-in `unittest` module.

Simply run:
`python3 -m unittest TestCrackerBarrelTriangle.py`
and you can run a set of unit tests on the code.

## Where did the sexy art on this README come from?
Art was shamelessly ripped off from Joe Whitt from
[here](http://obligatorymorningfart.tumblr.com/image/144269156464).
