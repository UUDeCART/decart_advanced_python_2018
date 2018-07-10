"""
Basic vector operations created as class exercise
"""
import math

def vec_eq(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors are of unequal length")

    for i in range (len(v1)):
        if v1[i] != v2[i]:
            return False

    return True

def v_plus_v(v1, v2):
    return [vec1 + vec2 for vec1, vec2 in zip(v1,v2)]

def alpha_x_v(alpha, v):
    return [vec*alpha for vec in v]

def vector_norm(vec):
    """
    Norms a vector_norm
    """
    return math.sqrt(sum([v**2 for v in vec]))

def inner(v1,v2):
    return sum([e1 * e2 for e1,e2 in zip(v1,v2)])
