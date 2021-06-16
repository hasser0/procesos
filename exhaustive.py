from itertools import product
from util import stable_vector
import numpy as np

def exhaustive(Pijk, Cik):
    m, k = Cik.shape
    z_best = np.infty
    politic_best = None
    decisions = [i for i in range(k)]
    for politic in product(decisions, repeat=m):
        P = np.array([Pijk[i, :, k] for i, k in enumerate(politic)])
        C = np.array([Cik[i, k] for i, k in enumerate(politic)])
        if np.isnan(P).any() or np.isnan(C).any():
            continue
        PI = stable_vector(P)
        cur_z = (C @ PI)[0]
        print("-" * 15 + "Política " + str(politic) + "-" * 15)
        print(PI)
        print(cur_z)
        print()
        if cur_z < z_best:
            z_best = cur_z
            politic_best = politic
    print("-"*15+"Mejor política"+"-"*15)
    print(politic_best)
    print(z_best)
    return np.array(politic_best), z_best