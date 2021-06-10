import numpy as np
from itertools import product


def improvement(Pijk, Cik):
    m, k = Cik.shape
    C = None
    P = None
    R1 = None
    decisions = [x for x in range(k)]
    for politic in product(decisions, repeat=m):
        C = np.array([Cik[i, kei] for i, kei in enumerate(politic)]).reshape(-1, 1)
        if np.isnan(C).any():
            continue
        P = np.array([Pijk[i, :, kei] for i, kei in enumerate(politic)])
        R1 = politic
        break
    new_politic = np.array(R1)
    previous_politic = np.ones(m)*-1
    while not (previous_politic==new_politic).all():
        previous_politic = new_politic
        C = np.array([Cik[i, kei] for i, kei in enumerate(previous_politic)]).reshape(-1, 1)
        P = np.array([Pijk[i, :, kei] for i, kei in enumerate(previous_politic)])
        P = np.eye(m) - P
        P[:, m - 1] = 1
        vj = np.linalg.inv(P) @ C
        gR = vj[m - 1][0]
        vj[m - 1] = 0
        new_politic = []
        for state in range(m):
            pol = np.nanargmin((Cik[state, :].reshape(-1, 1) + (Pijk[state, :, :].T @ vj) - vj[state]).flatten())
            new_politic.append(pol)
        new_politic = np.array(new_politic)
    return new_politic

def improvementd(Pijk, Cik, alpha=0.9):
    m, k = Cik.shape
    C = None
    P = None
    R1 = None
    decisions = [x for x in range(k)]
    for politic in product(decisions, repeat=m):
        C = np.array([Cik[i, kei] for i, kei in enumerate(politic)]).reshape(-1, 1)
        if np.isnan(C).any():
            continue
        P = np.array([Pijk[i, :, kei] for i, kei in enumerate(politic)])
        R1 = politic
        break
    new_politic = np.array(R1)
    previous_politic = np.ones(m) * -1
    while not (previous_politic == new_politic).all():
        previous_politic = new_politic
        C = np.array([Cik[i, kei] for i, kei in enumerate(previous_politic)]).reshape(-1, 1)
        P = np.array([Pijk[i, :, kei] for i, kei in enumerate(previous_politic)])
        P = np.eye(m) - alpha * P
        vj = np.linalg.inv(P) @ C
        new_politic = []
        for state in range(m):
            pol = np.nanargmin((Cik[state, :].reshape(-1, 1) + alpha*(Pijk[state, :, :].T @ vj)).flatten())
            new_politic.append(pol)
        new_politic = np.array(new_politic)
    return new_politic
