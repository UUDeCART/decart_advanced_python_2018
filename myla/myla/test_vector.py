import vector
import unittest
import math

def test_vector_equality_unequal_length():
    v1 = [1] * 2
    v2 = [1] * 3
    vector.vec_eq(v1,v2)

def test_norm():
    assert(vector.vector_norm([1,2,3]) == math.sqrt(1**2 + 2**2 + 3**2))

test_norm()
