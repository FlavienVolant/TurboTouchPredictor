# Gery Casiez
# 2024

import os
import math
import sys
import pandas
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('implementation')
parser.add_argument('filename')
args = parser.parse_args()

if not(os.path.isfile(args.filename)):
    print("%s does not exist"%args.filename, file=sys.stderr)
    sys.exit()

try:
    df = pandas.read_csv('strokesPredicted64GroundTruth.csv')
except:
    df = pandas.read_csv('../strokesPredicted64GroundTruth.csv')
df2 = pandas.read_csv(args.filename)

problem = False

if df.shape[0] != df2.shape[0]:
    print("The test file does not have the correct number of lines.", file=sys.stderr)
    sys.exit()

for (index, row), (index2, row2) in zip(df.iterrows(), df2.iterrows()):
    if math.fabs(row['When'] - row2['When']) > 0.01:
        print("line %s: timestamps are different : %s != %s"%(index+2, row['timestamp'], row2['timestamp']), file=sys.stderr)
        problem = True
        break
    if math.fabs(row['predX'] - row2['predX']) > 0.01:
        print("line %s: predX data is different: %s != %s"%(index+2, row['predX'], row2['predX']), file=sys.stderr)
        problem = True
        break
    if math.fabs(row['predY'] - row2['predY']) > 0.01:
        print("line %s: predY data is different: %s != %s"%(index+2, row['predY'], row2['predY']), file=sys.stderr)
        print("Check your parameters or your implementation")
        problem = True
        break

if problem:
    print("::error Problem with %s checking"%args.implementation, file=sys.stderr)
    sys.exit(1)
else:
    print("\n>>>>>> %s implementation looks good. <<<<<<\n"%args.implementation)