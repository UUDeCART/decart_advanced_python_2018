"""
utility funcs for myla for DeCART adv Python
"""

from sympy.abc import x, y, z
from sympy.plotting import plot, plot3d
import sympy as sp
from sympy import solve, symbols

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
x1,x2 = symbols('x1 x2')


def plot_lines(*eqs, solvefor='y'):
    plot(*[solve(e,solvefor)[0] for e in eqs])

def plot_vectors(*vs):
    ps = []
    tipx = []
    tipy = []
    tipc = []
    for v in vs:
        ps.append((v[0][0],v[0][0]+v[1][0]))
        ps.append((v[0][1],v[0][1]+v[1][1]))
        ps.append(v[2])
        tipx.append(v[0][0]+v[1][0])
        tipy.append(v[0][1]+v[1][1])
        tipc.append(v[2])
    plt.plot(*ps)
    plt.scatter(tipx, tipy)


def create_vd(v):
    if isinstance(v[0], np.ndarray):
        return (0,0,v[0][0],v[0][1])
    else:
        return (0,0,v[0],v[1])
def extract_color(v):
    if isinstance(v[0], np.ndarray):
        return v[1]
    else:
        return v[2]

def draw_vectors(*v, ax=None):

    vs = [create_vd(vv) for vv in v]
    soa =np.array(vs)
    X, Y, U, V = zip(*soa)
    if ax == None:
        plt.figure()
        ax = plt.gca()

    maxx = np.abs(soa.max())


    colors = [extract_color(vv) for vv in v]
    ax.quiver(X, Y, U, V, color = colors, angles='xy', scale_units='xy', scale=1)

    ax.set_xlim([-1.2*maxx, 1.2*maxx])
    ax.set_ylim([-1.2*maxx, 1.2*maxx])
    ax.set_aspect("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.draw()
    plt.show()
