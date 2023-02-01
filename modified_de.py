from scipy.optimize._differentialevolution import differential_evolution, DifferentialEvolutionSolver

# FuzzySet, FILE, DE (DE.Problem, DE.Optimizer, DE.SearchControls, DE.BestStrategy, DE.Ranges, DE.RandStrategy) class ve ya tipleri ZFIS.cs faylinda yoxdur

class Function:
    def __init__(self, c, bounds, A_ub=None, b_ub=None) -> None:
        self.c = c
        self.bounds = bounds
        self.A_ub = A_ub
        self.b_ub = b_ub
        self.n = len(c)
        self.m = len(b_ub)

    def f(self, x):
        summation_base = 0

        summation_base += (4*x[0] + x[1])
        summation_base += (3*x[0] + x[1] - 3)
        summation_base += (4*x[0] + 3*x[1] - x[2] - 6)
        summation_base += (x[0] + 2*x[1] + x[3] - 4)

        # summation = 0
        # for index in range(self.n):
        #     summation += self.c[index] * x[index]
        # summation_base += summation ** 2

        # for j in range(self.m):
        #     summation = 0
        #     for index in range(self.n):
        #         summation += self.A_ub[j][index] * x[index]
        #     summation -= self.b_ub[j]
        #     summation_base += summation ** 2
        
        # for index in range(self.n):
        #     summation_base += self.c[index] * x[index]

        # for j in range(self.m):
        #     for index in range(self.n):
        #         summation_base += self.A_ub[j][index] * x[index]
        #     summation_base -= self.b_ub[j]

        # summation_base **= 2

        # summation = 0
        # for index in range(self.n):
        #     summation += self.c[index] * x[index]
        # summation_base += summation ** 2

        # summation = 0
        # for j in range(self.m):
        #     for index in range(self.n):
        #         summation += self.A_ub[j][index] * x[index]
        #     summation -= self.b_ub[j]
        # summation_base += summation ** 2

        return summation_base

function = Function(c=[4, 1, 0, 0], bounds=[(0.1, 1), (1, 2), (0, 0.0001), (0, 0.0001)], A_ub=[
    [3, 1, 0, 0],
    [4, 3, -1, 0],
    [1, 2, 0, 1]
], b_ub=[3, 6, 4])


def f(x):
    summation_base = 0

    # summation_base += (4*x[0] + x[1]) ** 2
    # summation_base += (3*x[0] + x[1] - 3) ** 2
    # summation_base += (4*x[0] + 3*x[1] - x[2] - 6) ** 2
    # summation_base += (x[0] + 2*x[1] + x[3] - 4) ** 2

    summation_base += (x[4] + x[5] + x[6]) ** 2
    summation_base += (3*x[0] + x[1] + x[4] - 3) ** 2
    summation_base += (4*x[0] + 3*x[1] - x[2] + x[5] - 6) ** 2
    summation_base += (x[0] + 2*x[1] + x[3] + x[6] - 4) ** 2

    return summation_base

bounds = [(0, 4), (0, 4), (0, 0.001), (0, 0.001), (0, 0.001), (0, 0.001), (0, 0.001)]

print(differential_evolution(func=f, bounds=bounds, popsize=100, maxiter=2000))

# differential_evolution_solver = DifferentialEvolutionSolver(func=function.f, bounds=function.bounds, popsize=50)

# print(differential_evolution_solver.solve())
