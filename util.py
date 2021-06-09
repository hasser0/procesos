import numpy as np

def stable_vector(P):
    size = P.shape[0]
    PI = np.eye(size)-P.T
    ones = np.ones(size).reshape(1,-1)
    PI = np.concatenate((PI,ones),axis=0)
    PI = PI[1:,]
    b = np.zeros(size).reshape(-1,1)
    b[size-1,0] = 1
    return np.linalg.inv(PI) @ b
def first_visit_prob(P,j):
    size = P.shape[0]
    indexes = np.ones(size, dtype=bool)
    indexes[j] = False
    P_red = P[indexes][:,indexes]
    P_red = np.eye(size-1) - P_red
    b = np.ones(size-1).reshape(-1,1)
    return np.linalg.inv(P_red) @ b
def absortion_prob(P,j):
    size = P.shape[0]
    is_nabsorb = np.array([False if P[i,i]==1 else True for i in range(size)])
    nabsorb = is_nabsorb.sum()
    P_red = np.eye(nabsorb) - P[is_nabsorb][:,is_nabsorb]
    b = P[:,j][is_nabsorb].reshape(-1,1)
    return np.linalg.inv(P_red) @ b