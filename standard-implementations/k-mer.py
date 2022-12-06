from collections import defaultdict

with open('../dataset/NC_000009.12[99800001..105400000].fa', 'r') as f:
  lines = f.readlines()
  s = ''.join(list(map(lambda l: l.strip(), lines[1:])))

  K_MER_SIZE = 50
  # AABC
  k = K_MER_SIZE
  hm = defaultdict(lambda: 0)
  for i in range(len(s) - k):
    hm[s[i: i + k]] += 1

  pairs = []
  for k in hm:
    v = hm[k]
    if v >= 20:
      pairs.append('' + str(k) + ": " + str(v))
  
  f.close()

  with open('./output.txt', 'w') as f:
    f. write('\n'.join(pairs))

