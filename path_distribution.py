import sys
probs = {"11": [(15./36, lambda p: (p[0], p[1]-1)),
                (21./36, lambda p: (p[0]-1, p[1]))],
         "21": [(125./216, lambda p: (p[0], p[1]-1)),
                (91./216, lambda p: (p[0]-1, p[1]))],
         "31": [(855./1296, lambda p: (p[0], p[1]-1)),
                (441./1296, lambda p: (p[0]-1, p[1]))],
         "12": [(55./216, lambda p: (p[0], p[1]-1)),
                (161./216, lambda p: (p[0]-1, p[1]))],
         "22": [(295./1296, lambda p: (p[0], p[1]-2)),
                (420./1296, lambda p: (p[0]-1, p[1]-1)),
                (581./1296, lambda p: (p[0]-2, p[1]))],
         "32": [(2890./7776, lambda p: (p[0], p[1]-2)),
                (2611./7776, lambda p: (p[0]-1, p[1]-1)),
                (2275./7776, lambda p: (p[0]-2, p[1]))]
         }

lower_limit = 10 ** -20
exceed_count = 0

def get_key(a_num, d_num):
  if a_num < 2 or d_num < 1:
    return False
  attack = min(3, a_num - 1)
  defence = min(2, d_num)
  return str(attack) + str(defence)

def calc_prob(init_prob, attack, defence):
  if not init_prob:
    return {}
  exceed_count = 0
  dist = {}
  for i in range(attack):
    dist[i] = 0
  pair = [init_prob, (attack, defence)]
  lst = [pair]
  while lst:
    new = []
    for p in lst:
      key = get_key(*p[1])
      if not key: continue
      for case in probs[key]:
        prob = case[0] * p[0]
        if prob < lower_limit:
          exceed_count += 1
          continue
        next_pair = case[1](p[1])
        if next_pair[0] <= 1:
          dist[0] += prob
        elif next_pair[1] <= 0:
          attack_win_move = next_pair[0] - 1
          dist[attack_win_move] += prob
        else:
          new.append([prob, next_pair])
    lst = new[:]
  if exceed_count: print "EXCEED", exceed_count
  return dist



argc = len(sys.argv)
if argc < 3:
  print "Argument form: {number attacking} {number defending ...}"
  sys.exit()
try:
  a = int(sys.argv[1])
  d = [int(sys.argv[i]) for i in range(2, argc)]
except ValueError:
  print "Non-numeric argument passed"
  sys.exit()

dist = {}
old_dist = {}
for defence in d:
  if dist:
    old_dist = dist
  # Recurring fights use the last distribution
  if old_dist:
    dist = {}
    for i in range(a):
      dist[i] = 0
    for key in old_dist:
      if key < 2:
        dist[0] += old_dist[key]
      else:
        new_dist = calc_prob(old_dist[key], key, defence)
        for nkey in new_dist:
          dist[nkey] += new_dist[nkey]
  # The first fight of the sequence will have dist be unset
  else:
    dist = calc_prob(1, a, defence)

for key in reversed(sorted(dist.keys())):
  #if not dist[key]: continue
  name = "LOSS" if key == 0 else key
  print name, ":", "%.2f" % (dist[key] * 100)
