import matplotlib.pyplot as plt
import numpy as np

def draw_vectors(*v, ax=None):
    """
    draws vectors on a matplotlib axis
    """
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
