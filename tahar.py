import random as rd
from scipy.optimize import differential_evolution as de
from zClass import *
from Z_module import *
import numpy as np
import time 

def sorting(arr):
    for i in range(len(arr)):
        arr[i] = np.sort(arr[i])

    return arr

def operations_on_coefficients(arr):
    a = sorting(arr[0 : 8].reshape(2, 4))
    b = sorting(arr[8 : 16].reshape(2, 4))
    c = sorting(arr[16 : 24].reshape(2, 4))

    a = z_ededleri(str(a.tolist()))
    b = z_ededleri(str(b.tolist()))
    c = z_ededleri(str(c.tolist()))

    return (a, b, c)

def generatingZ(arr):
    object_arr = np.ndarray((len(arr), ), dtype=object)

    for i in range(len(arr)):
        res = np.empty((2, 4), dtype=float)

        centre = arr[i][0]
        res[0][1] = res[0][2] = centre
        res[0][0] = centre - arr[i][1]
        res[0][3] = centre + arr[i][2]

        start = 0.1

        for j in range(4):
            if j == 2:
                res[1][j] = res[1][j - 1]
            else:
                num = rd.uniform(start, 1.0)
                res[1][j] = num
                start = num
            
        zNum = str(res.tolist())
        object_arr[i] = z_ededleri(zNum)

    return object_arr

def functionEvaluater(object_x1, object_x2, object_y, arr):
    a, b, c = operations_on_coefficients(arr)

    start = time.time()
    similarity = 0

    for i in range(len(object_x1)):
        result_equation = a * object_x1[i] * object_x1[i] + b * object_x2[i] * object_x2[i] + c * object_x1[i] * object_x2[i]
        calculated_y = extract(result_equation.value)

        accurate_y = extract(object_y[i].value)
        similarity+= 1 - calculate_similarity(calculated_y, accurate_y, 'Hellinger-Hausdorff')

    print(time.time() - start)
    return similarity


x1 = np.array([
    [0.1, 0.1, 0.1],
    [0.3, 0.2, 0.1],
    [0.6, 0.2, 0.2],
    [0.9, 0.1, 0.3],
    [0.7, 0.1, 0.1],
    [0.5, 0.1, 0.1],
    [0.1, 0.1, 0.1],
    [0.7, 0.1, 0.1],
    [0.5, 0.1, 0.1],
    [0.1, 0.1, 0.1]
])

x2 = np.array([
    [0.1, 0.1, 0.1],
    [0.1, 0.1, 0.2],
    [0.5, 0.2, 0.1],
    [0.5, 0.3, 0.4],
    [0.95, 0.05, 0.05],
    [0.6, 0.4, 0.3],
    [0.5, 0.2, 0.1],
    [0.6, 0.4, 0.3],
    [0.5, 0.3, 0.4],
    [0.8, 0.1, 0.1]
])

y = np.array([
    [0.037, 0.120, 0.129],
    [-0.005, 0.233, 0.450],
    [0.912, 1.470, 1.372],
    [0.729, 2.394, 3.339],
    [3.405, 1.325, 1.750],
    [1.360, 2.305, 2.068],
    [0.861, 0.883, 0.542],
    [1.321, 2.568, 2.504],
    [0.937, 1.586, 2.194],
    [2.149, 0.967, 0.924]
])

object_x1 = generatingZ(x1)
object_x2 = generatingZ(x2)
object_y = generatingZ(y)


bounds_for_coefficient = [
    [-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],    [0.9, 1], [0.9, 1], [0.9, 1], [0.9, 1], #A
    [3, 4], [3, 4], [3, 4], [3, 4],                        [0.9, 1], [0.9, 1], [0.9, 1], [0.9, 1], #B
    [1, 2], [1, 2], [1, 2], [1, 2],                        [0.9, 1], [0.9, 1], [0.9, 1], [0.9, 1]  #C
]

res = de(lambda arr : functionEvaluater(object_x1, object_x2, object_y, arr), bounds=bounds_for_coefficient, maxiter=2, popsize=4)

a = sorting(res.x[0 : 8].reshape(2, 4))
b = sorting(res.x[8 : 16].reshape(2, 4))
c = sorting(res.x[16 : 24].reshape(2, 4))

for x in object_x1:
    print(x.value)

print('\n')
for x in object_x2:
    print(x.value)

print('\n')
for x in object_y:
    print(x.value)

print('\n')
print('a = ', a)
print('b = ', b)
print('c = ', c)