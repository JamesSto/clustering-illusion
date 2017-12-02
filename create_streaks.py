from random import random, choice
from termcolor import colored


HIT = colored("H", 'green')
MISS = colored("M", 'red')

def create_streak(length, bias):
	streak = []
	streak.append(choice([HIT, MISS]))
	for _ in xrange(length-1):
		prev = streak[-1]
		if random() < bias:
			streak.append(prev)
		else:
			streak.append(MISS if prev == HIT else HIT)
	return streak


rec = []
for _ in xrange(10):
	if random() < .5:
		print " ".join(create_streak(10, 0.7))
		rec.append("streaky")
	else:
		print " ".join(create_streak(10, .5))
		rec.append("normal")
	print ""

for x in rec:
	print x
