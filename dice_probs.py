from itertools import product as prod
from random import randint as rand

combos = [list(prod(range(1,7), repeat=r)) for r in range(2,6)]

wins = 0
for combo in combos[0]:
  if combo[0] > combo[1]:
    wins += 1
print "1 on 1 : ", wins, len(combos[0]), 1.0 * wins / len(combos[0])

wins = 0
for combo in combos[1]:
  if combo[0] > combo[2]:
    wins += 1
  elif combo[1] > combo[2]:
    wins += 1
print "2 on 1 : ", wins, len(combos[1]), 1.0 * wins / len(combos[1])

wins = 0
for combo in combos[2]:
  if combo[0] > combo[3]:
    wins += 1
  elif combo[1] > combo[3]:
    wins += 1
  elif combo[2] > combo[3]:
    wins += 1
print "3 on 1 : ", wins, len(combos[2]), 1.0 * wins / len(combos[2])


wins = 0
for combo in combos[1]:
  if combo[0] > combo[1] and combo[0] > combo[2]:
    wins += 1
print "1 on 2 : ", wins, len(combos[1]), 1.0 * wins / len(combos[1])

wins = 0
ties = 0
losses = 0
for combo in combos[2]:
  a = sorted(combo[:2])
  d = sorted(combo[2:])
  small = a[0] > d[0]
  big = a[1] > d[1]
  if small and big:
    wins += 1
  elif small or big:
    ties += 1
  else:
    losses += 1
print "2 on 2 : "
print "\tWin 2  : ", wins, len(combos[2]), 1.0 * wins / len(combos[2])
print "\tTie    : ", ties, len(combos[2]), 1.0 * ties / len(combos[2])
print "\tLose 2 : ", losses, len(combos[2]), 1.0 * losses / len(combos[2])

wins = 0
ties = 0
losses = 0
for combo in combos[3]:
  a = sorted(combo[:3])[1:]
  d = sorted(combo[3:])
  small = a[0] > d[0]
  big = a[1] > d[1]
  if small and big:
    wins += 1
  elif small or big:
    ties += 1
  else:
    losses += 1
print "3 on 2 : "
print "\tWin 2  : ", wins, len(combos[3]), 1.0 * wins / len(combos[3])
print "\tTie    : ", ties, len(combos[3]), 1.0 * ties / len(combos[3])
print "\tLose 2 : ", losses, len(combos[3]), 1.0 * losses / len(combos[3])

