import pandas as pd
import numpy as np
import argparse


def inner(v1,v2):
    return sum([x*y for x,y in zip(v1,v2)])

def m_x_v(m,v):
    new_v = np.zeros(v.shape, dtype=np.float64)
    for i in range(m.shape[1]):
        new_v = new_v + v[i]*m[:,i]
    return new_v

def m_x_m(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    #C = []
    for j in range(B.shape[1]):
        c = m_x_v(A,B[:,j])
        C[:,j] = c # m_x_v(A,B[:,j])
    return C


def inner(v1,v2):
    return sum([x*y for x,y in zip(v1,v2)])

def m_x_v(m,v):
    new_v = np.matrix(np.zeros((m.shape[0],1), dtype=np.float64))

    for i in range(m.shape[1]):
        new_v = new_v + (float(v[i])*m[:,i])
    return new_v

def m_x_m(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    #C = []
    for j in range(B.shape[1]):
        c = m_x_v(A,B[:,j])
        C[:,j] = c.flat # m_x_v(A,B[:,j])
    return C


def find_pivot2(c):
    return np.argmax(c)

def find_pivot(c):
    m = c.shape[0]
    maxv = c[0]
    argmax = 0
    for i in range(1,m):
        if c[i] > maxv:
            maxv = c[i]
            argmax = i

    return argmax

def swap_rows(a,i,j):
    A = np.matrix.copy(a)
    tmp = A[i,:].copy()
    A[i,:] = A[j,:].copy()
    A[j,:] = tmp
    return A

def pivot_rows(a,k):
    # find pivot
    pivot_row = find_pivot(a[k:,k]) + k
    A = swap_rows(a,k,pivot_row)
    return A


def gaussian_elimination2(a,_b):
    Ab = np.concatenate([a,_b],axis=1).astype(np.float64)

    # number of rows
    m = Ab.shape[0]
    for k in range(0,m-1):

        Ab = pivot_rows(Ab,k)
        for i in range(k+1,m):

            f = Ab[i,k]/Ab[k,k]
            Ab[i,:] = Ab[i,:]-f*Ab[k,:]

    return Ab[:,:-1],Ab[:,-1]

def backward_solve(U, b):
    x = np.zeros(b.shape)
    m = U.shape[0]
    for i in range(m-1,-1,-1):
        s = b[i]
        for j in range(i+1,m):
            s = s-U[i,j]*x[j]
        x[i] = s/U[i,i]
    return x


def transpose(a):
    out = np.zeros((a.shape[1],a.shape[0]), dtype=a.dtype)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            out[j,i] = a[i,j]
    return np.matrix(out)

def main():

    parser = argparse.ArgumentParser(description='Profiling my least squares.')

    parser.add_argument('--test', dest='tester', action='store_true')
    args = parser.parse_args()

    if args.tester:
        print("running test")
        A = np.matrix([[1,2,1],[3,8,1],[0,4,1]],dtype=np.float64)
        b = np.matrix([2,12,2], dtype=np.float64).transpose()
    else:
        data = pd.read_table("https://archive.ics.uci.edu/ml/machine-learning-databases/00243/yacht_hydrodynamics.data",
                      header=None,
                      delimiter="\s+",
                      error_bad_lines=False)
        A = np.matrix(data.iloc[:,:-1].values)
        b_ = np.matrix(data.iloc[:,-1].values).transpose()
        """print("running slice detector")
        data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00206/slice_localization_data.zip",
                        compression="zip")
        A = np.matrix(data.iloc[:200,1:5].values)
        b_ = np.matrix(data["reference"].values[:200]).transpose()"""
        A = m_x_m(transpose(A),A)
        print(A.shape)
        b = m_x_v(transpose(A),b_)
        print(b.shape)
    U,b2 = gaussian_elimination2(A,b)
    x = backward_solve(U,b2)
    print(x)

if __name__ == "__main__":
    main()
