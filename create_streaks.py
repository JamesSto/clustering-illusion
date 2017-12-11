from __future__ import division
from random import random, randint, uniform
from termcolor import colored
from tqdm import tqdm

HIT = "H"
MISS = "M"

class Streak(object):
    def __init__(self, avg, sequence):
        self.avg = avg
        self.sequence = sequence

        total_hits = 0
        streaks = 0
        for p, n in zip(self.sequence, self.sequence[1:]):
            if p == HIT:
                total_hits += 1
                if n == HIT:
                    streaks += 1

        self.streakiness = streaks/total_hits if total_hits else None

    def is_streaky(self):
        return self.streakiness > self.avg

    def __str__(self):
        avg = str(round(self.avg,2))
        streakiness = str(round(self.streakiness,2))
        sequence = " ".join(self.sequence)
        return avg + "," + streakiness + "," + str(self.is_streaky()) + "," + sequence

def create_streak(length, avg):
    sequence = []
    for _ in xrange(length):
        if random() < avg:
            sequence.append(HIT)
        else:
            sequence.append(MISS)
    
    return Streak(avg, sequence)


s = []
print "avg,streakiness,is_streaky,sequence"
for _ in xrange(500):
    x = create_streak(50, uniform(0.3, 0.9))
    print x
    s.append(x)
