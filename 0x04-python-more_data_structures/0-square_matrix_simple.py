#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map((lambda x: x * x), elm)) for elm in matrix]
