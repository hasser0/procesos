import numpy as np

def succesive(Pijk, Cik, n=10, alpha=0.9):
    m, k = Cik.shape
    iteration = 0
    politic = np.nanargmin(Cik, axis=1)
    V = np.nanmin(Cik, axis=1).reshape(-1,1)
    while iteration < n:
        politic = []
        new_V = []
        for state in range(m):
            Vj = np.nanmin((Cik[state, :].reshape(-1,1) + alpha*Pijk[state, :, :].T @ V).flatten())
            pol = np.nanargmin((Cik[state, :].reshape(-1, 1) + alpha * Pijk[state, :, :].T @ V).flatten())
            politic.append(pol)
            new_V.append(Vj)
        V = np.array(new_V).reshape(-1,1)
        iteration+=1
    return politic