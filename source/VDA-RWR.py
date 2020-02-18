import numpy as np

def fun(A, SD, SV, lam, alpha, r):
    Nv, Nd = A.shape

    KD = SD
    KV = SV

    HVV = np.zeros((Nv, Nv))
    HVD = np.zeros((Nv, Nd))
    HDD = np.zeros((Nd, Nd))
    HDV = np.zeros((Nd, Nv))

    for i in range(Nv):
        S = np.sum(A[i])
        dvi = np.sum(KV[i])
        for j in range(Nv):
            if S:
                HVV[i][j] = (1 - lam) * KV[i][j] / dvi
            else:
                HVV[i][j] = KV[i][j] / dvi

    for i in range(Nv):
        S = np.sum(A[i])
        for j in range(Nd):
            if S:
                HVD[i][j] = lam * (A[i][j]) / S
            else:
                HVD[i][j] = 0


    for i in range(Nd):
        dvi = np.sum(KD[i])
        for j in range(Nd):
            if np.sum(A[:, j]):
                HDD[i][j] = (1 - lam) * KD[i][j] / dvi
            else:
                HDD[i][j] = KD[i][j] / dvi

    for i in range(Nd):
        for j in range(Nv):
            if np.sum(A[:, i]):
                HDV[i][j] = lam * A[j][i] / np.sum(A[:, i])
            else:
                HDV[i][j] = 0

    temp1 = np.hstack((HVV, HVD))
    temp2 = np.hstack((HDV, HDD))
    H = np.vstack((temp1, temp2))

    prst = alpha * np.eye(Nv)
    prst = np.vstack((prst, np.full((Nd, Nv), (1 - alpha) / Nd)))
    pst = prst.copy()
    change = 1
    while change > 10e-12:
        new_pst = (1 - r) * np.matmul(H.transpose(), pst) + r * prst
        error = new_pst - pst
        change = np.linalg.norm(error)
        pst = new_pst.copy()

    return pst[Nv::, :]


