import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--source", help="Source file of DNA Sequences in FASTA format")
parser.add_argument("-o", "--output", help="Output directory")
parser.add_argument("-j", "--jobcount", help="Number of files to produce", type=int, default=10)
parser.add_argument("-k", "--kval", help="Size of k-mer", type=int)

args = parser.parse_args()

jobs = []

with open(args.source, 'r') as f:
  lines = f.readlines()
  s = ''.join(list(map(lambda l: l.strip(), lines[1:])))

  T = len(s)
  f = args.jobcount
  k = args.kval
  L = 0 # We need to calculate this amount

  L = math.ceil(T / f)

  i = 0
  for i in range(0, T, L): 
    jobs.append(s[i: i + L])


  overlaps = []
  if k < L:
    for idx in range(len(jobs) - 1):
      s1 = jobs[idx][len(jobs[idx]) - k + 1:]
      s2 = jobs[idx + 1][0: k - 1]
      for j in range(len(s1)): 
        overlaps.append(s1[j:] + s2[: k - (len(s1) - j)])
    
    jobs.append('\n'.join(overlaps))

  for i, s in enumerate(jobs):
    f = open(args.output + '/file' + str(i + 1) + '.txt', 'w')
    f.write(s)
    f.close()
