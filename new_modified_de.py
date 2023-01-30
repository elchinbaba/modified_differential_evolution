from scipy.optimize._differentialevolution import DifferentialEvolutionSolver

class Function:
    def __init__(self, c, bounds, A_ub=None, b_ub=None) -> None:
        self.c = c
        self.bounds = bounds
        self.A_ub = A_ub
        self.b_ub = b_ub
        self.n = len(c)
        self.m = len(b_ub)

    def set_differential_evalution_solver(self, differential_evolution_solver):
        self.differential_evolution_solver = differential_evolution_solver
        self.set_population(differential_evolution_solver.population)
    
    def set_population(self, population):
        self.population = population

    def f(self, x):
        summation_base = 0
        for agent in self.population:
            summation = 0
            for index in range(self.n):
                summation += self.c[index] * agent[index]
            summation_base += summation ** 2

            for j in range(self.m):
                summation = 0
                for index in range(self.n):
                    summation += self.A_ub[j][index] * agent[index]
                summation -= self.b_ub[j]
                summation_base += summation ** 2

        self.set_population(self.differential_evolution_solver.population)

        return summation_base

function = Function(c=[4, 1], bounds=[(0, 4) for _ in range(2)], A_ub=[
    [3, 1],
    [4, 3],
    [1, 2]
], b_ub=[3, 6, 4])
differential_evolution_solver = DifferentialEvolutionSolver(func=function.f, bounds=function.bounds)
function.set_differential_evalution_solver(differential_evolution_solver)

print(function.differential_evolution_solver.solve())
