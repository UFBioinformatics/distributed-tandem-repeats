from collections import defaultdict
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--source", help="Source file of DNA Sequences in FASTA format")
parser.add_argument("-o", "--output", help="Output file for the result", nargs="?", const="ARG_NOT_GIVEN")
parser.add_argument("-k", "--kval", help="Size of k-mer", type=int)

args = parser.parse_args()

with open(args.source, 'r') as f:
  lines = f.readlines()
  s = ''.join(list(map(lambda l: l.strip(), lines[1:])))
  k = args.kval
  
  hm, pairs = defaultdict(lambda: 0), []
  for i in range(len(s) - k + 1): hm[s[i: i + k]] += 1

  for k in hm: pairs.append(str(k) + " " + str(hm[k]))
  f.close()

  if args.output != 'ARG_NOT_GIVEN':
    with open(args.output, 'w') as f: f. write('\n'.join(pairs))
    f.close()
  else:
    print('\n'.join(pairs))

