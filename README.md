risk
====

Given an initial number of attacking armies and a sequence of defending armies, generates the distribution of attacking armies that will make it to the final territory.

Essentially, this tool is designed for the situation in the game of risk in which an attacking player wants to know how many pieces they can expect to end up with after a series of attacks. This can be useful in weighing two different attacking options or simply in better understanding the odds of an attack.

Calling form:
path\_distribution.py {number of attacking armies} {number of defending armies...}
Example:
Attacking with 10 armies
Want to attack a sequence of 3 territories with 1, 2, and 3 armies respectfully

Proper call is:
python path\_distribution.py 10 1 2 3
