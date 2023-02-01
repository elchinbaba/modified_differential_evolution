from scipy.optimize import differential_evolution
import numpy
import math

numpy.seterr(divide='ignore', invalid='ignore')
class Function:
    def __init__(self, c, bounds, A_gt=None, b_gt=None, A_lt=None, b_lt=None, A_eq=None, b_eq=None) -> None:
        self.c = c
        self.bounds = bounds
        self.n = len(c)
        self.A_gt = A_gt
        self.b_gt = b_gt
        self.A_lt = A_lt
        self.b_lt = b_lt
        self.A_eq = A_eq
        self.b_eq = b_eq

    def f(self, x):
        if self.A_eq:
            for j in range(len(self.A_eq)):
                sum_A_eq = 0
                for index in range(self.n):
                    sum_A_eq += self.A_eq[j][index] * x[index]
            
                # If equality constraint (a_j * x = b_j) does not hold then return such a big value that
                # does not optimize solution and forces the program to continue to iterate
                if not abs(sum_A_eq - self.b_eq[j]) < 0.3:
                    return numpy.inf

        if self.A_gt:
            for j in range(len(self.A_gt)):
                sum_A_gt = 0
                for index in range(self.n):
                    sum_A_gt += self.A_gt[j][index] * x[index]

                # If inequality constraint (a_j * x >= b_j) does not hold then return such a big value that
                # does not optimize solution and forces the program to continue to iterate
                if not sum_A_gt >= self.b_gt[j]:
                    return numpy.inf

        if self.A_lt:
            for j in range(len(self.A_lt)):
                sum_A_lt = 0
                for index in range(self.n):
                    sum_A_lt += self.A_lt[j][index] * x[index]

                # If inequality constraint (a_j * x <= b_j) does not hold then return such a big value that
                # does not optimize solution and forces the program to continue to iterate
                if not sum_A_lt <= self.b_lt[j]:
                    return numpy.inf

        fun = 0
        for index in range(self.n):
            fun += self.c[index] * x[index]

        return fun

# function = Function(c=[4, 1], bounds=[(-10, 10) for _ in range(2)],
#     A_eq=[[3, 1]], b_eq=[3], A_gt=[[4, 3]], b_gt=[6], A_lt=[[1, 2]], b_lt=[4])
# solution is [0.4, 1.8]

# function = Function(c=[-3, -1], bounds=[(0, 10) for _ in range(2)],
#     A_lt=[
#         [4, 3],
#         [4, 1],
#         [4, -1]
#     ], b_lt=[12, 8, 9])
# solution is [3/2, 2]

# function = Function(c=[-10, -1], bounds=[(0, 10) for _ in range(2)],
#     A_gt=[[4, -5]], b_gt=[5], A_lt=[[2, 11]], b_lt=[7])
# solution is [3.5, 0]

# function = Function(c=[-1, 3], bounds=[(0, 10) for _ in range(2)],
#     A_gt=[
#         [-5, -4],
#         [2, 1]
#     ], b_gt=[-9, -5],
#     A_lt=[
#         [3, -2]
#     ], b_lt=[3])
# solution is [1, 0]

# function = Function(c=[4, -1, 1], bounds=[(0, 10) for _ in range(3)],
#     A_eq=[
#         [-4, 1, -2],
#         [5, 2, 4]
#     ], b_eq=[-3, 2],
#     A_gt=[
#         [-2, -3, 3]
#     ], b_gt=[-1])
# solution does not exist

# function = Function(c=[-7, 7, -2], bounds=[(0, 10) for _ in range(3)],
#     A_eq=[[3, -1, 5]], b_eq=[3], A_gt=[[1, 2, -3]], b_gt=[5])
# solution is [11/7, 12/7, 0] ([1.57..., 1.71..., 0])

# function = Function(c=[3, 1, 8], bounds=[(0, 10) for _ in range(3)],
#     A_eq=[
#         [2, 5, 1],
#         [1, 2, -1],
#         [4, 9, -1]
#     ], b_eq=[5, 2, 9])
# solution is [0, 1, 0]

# function = Function(c=[5, 1, 1], bounds=[(0, 10), (-10, 10), (0, 10)],
#     A_eq=[
#         [2, -3, 2],
#         [1, -3, 1]
#     ], b_eq=[6, 6])
# solution is [0, -2, 0]

# function = Function(c=[-1, 1, -5], bounds=[(0, 10) for _ in range(3)],
#     A_eq=[
#         [2, 6, 1],
#         [1, 8, -1]
#     ], b_eq=[6, 8],
#     A_gt=[
#         [1, -1, -2]
#     ], b_gt=[-5])
# solution is [0, 1, 0]

# function = Function(c=[2, 1, -1], bounds=[(-10, 10), (0, 10), (0, 10)],
#     A_eq=[
#         [5, 3, 1],
#         [5, 1, -2]
#     ], b_eq=[10, 10],
#     A_lt=[
#         [-1, 1, 1]
#     ], b_lt=[1])
# solution is [2, 0, 0]

# function = Function(c=[-3, 1, -1], bounds=[(0, 10) for _ in range(3)],
#     A_eq=[
#         [1, 1, -1],
#         [2, 5, 4],
#         [-1, -4, -5]
#     ], b_eq=[1, 3, -2])
# solution is [7/6, 0, 1/6] ([1.1(6), 0, 0.1(6)])

print(differential_evolution(func=function.f, bounds=function.bounds, popsize=250))

def f(x):
    if abs(3*x[0] + x[1] - 3) > 0.01:
        return numpy.inf
    if 4*x[0] + 3*x[1] < 6:
        return numpy.inf
    if x[0] + 2*x[1] > 4:
        return numpy.inf

    return 4*x[0] + x[1]
# print(differential_evolution(func=f, bounds=[(-10, 10), (-10, 10)], popsize=100, maxiter=2000))

