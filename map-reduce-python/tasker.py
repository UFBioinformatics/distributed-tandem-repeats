
JOB_LENGTH = 1000
K_MER_LENGTH = 4

strs = []

with open('./dataset/NC_000009.12[99800001..105400000].fa', 'r') as f:
  lines = f.readlines()
  s = ''.join(list(map(lambda l: l.strip(), lines[1:])))
  pidx, cidx = 0, JOB_LENGTH
  while cidx < len(s):
    strs.append(s[pidx: cidx])
    pidx = cidx
    cidx += JOB_LENGTH
  
  strs.append(s[pidx: cidx])

if K_MER_LENGTH < JOB_LENGTH:
  for idx in range(len(strs) - 1):
    s1 = strs[idx][len(strs[idx]) - K_MER_LENGTH + 1:]
    s2 = strs[idx + 1][0: K_MER_LENGTH - 1]

    for j in range(len(s1)):
      strs.append(s1[j:] + s2[: K_MER_LENGTH - (len(s1) - j)])
    

for i, s in enumerate(strs):
  f = open('./map-reduce-python/input/file' + str(i + 1) + '.txt', 'w')
  f.write(s)
  f.close()
