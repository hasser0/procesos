from scipy.optimize import linprog
import numpy as np

def lp(Pijk, Cik):
    m, k = Cik.shape
    c = np.array([cik if cik != np.nan else 0 for cik in Cik.flatten()])
    c[np.isnan(c)] = 0
    yik = np.ones(m*k)
    yjk = np.array([[1 if jota == j else 0 for jota in range(m) for kei in range(k)] for j in range(m)])
    pij_yik = np.array([[Pijk[i, j, kei] for i in range(m) for kei in range(k)] for j in range(m)])
    pij_yik[np.isnan(pij_yik)]=0
    A = np.vstack((yik,yjk-pij_yik))
    b = np.zeros(m+1).reshape(-1,1)
    b[0,0] = 1
    print("Min z = c@y")
    print("donde")
    print("A@y<=b")
    print("c = "+str(c))
    print("A = "+str(A))
    print("b = "+str(b))
    res = linprog(c=c, A_eq=A, b_eq=b, method='revised simplex')
    print("-"*15+"Resultados"+"-"*15)
    print("z = "+str(res['fun']))
    print("yik = "+str(res['x']))
    return res['x'], res['fun']

