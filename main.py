import pandas as pd
import numpy as np
import argparse
from exhaustive import exhaustive
from lp import lp
from improvement import improvement, improvementd
from succesive import succesive

np.set_printoptions(suppress=True)
parser = argparse.ArgumentParser(description="Stochastic processes method's")
parser.add_argument('-f', '--file', type=str, help='File')
parser.add_argument('-M', '--states', type=int, help='Number of states')
parser.add_argument('-K', '--decisions', type=int, help='Number of decisions')
parser.add_argument('-m', '--method', type=str, help='Method to use')
args = parser.parse_args()

if __name__ == '__main__':
    file = args.file
    df = pd.read_excel(file, header=None)
    m = args.states
    k = args.decisions
    method = args.method
    pij = tuple(df.values[m*i:m*(i+1),0:m] for i in range(k))
    Pijk = np.dstack(pij)
    Cik = df.values[m*k:, 0:k]
    if method == 'exhaustive':
        best, z = exhaustive(Pijk, Cik)
        print(best)
        print(z)
    if method == 'linear':
        best, z = lp(Pijk, Cik)
        print(best.reshape(m,k))
        print(z)
    if method == 'improvement':
        print(improvement(Pijk, Cik))
    if method == 'improvementd':
        print(improvementd(Pijk, Cik))
    if method == 'succesive':
        print(succesive(Pijk, Cik))