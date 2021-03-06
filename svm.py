import numpy, random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Sample generator
num = 20
classA = numpy.concatenate(
    (numpy.random.randn(num, 2) * 0.2 + [1.5, 1],
     numpy.random.randn(num, 2) * 0.2 + [-1.5, 1]))
classB = numpy.random.randn(num*2, 2) * 0.2 + [0, 0.3]

inputs = numpy.concatenate((classA, classB))
targets = numpy.concatenate(
    (numpy.ones(classA.shape[0]),
     -numpy.ones(classB.shape[0])))

N = inputs.shape[0]

permute = list(range(N))
random.shuffle(permute)
inputs = inputs[permute, :]
targets = targets[permute]

# Kernel function
def kernel(a, b):

    return result

# Matrix for objective function
P = [[targets[i] * targets[j] * kernel(inputs[i], inputs[j]) for j in range(N)] for i in range(N)]

# Objective function
def objective(alpha):
    result = numpy.dot(alpha, numpy.dot(P, alpha)) * 0.5 - numpy.sum(alpha)
    return result

# zerofun
def zerofun(alpha):
    result = numpy.dot(alpha, targets)
    return result

# minimize
C = 1000
start = numpy.zeros(N)
B = [(0, C) for b in range(N)]
XC = {'type':'eq', 'fun':zerofun}
ret = minimize(objective, start, bounds = B, constraints = XC)
min_alpha = ret['x']
print (ret['success'])

# find support vector
SV = [i for i in range(N) if min_alpha[i] > 0.00001]

# calculate b
b = numpy.dot(min_alpha, P[SV[0]]) * targets[SV[0]] - targets[SV[0]]

# indicator
def indicator(x, y):
    result = numpy.dot(min_alpha, [targets[i] * kernel(inputs[i], [x, y]) for i in range(N)]) - b
    return result

plt.plot([p[0] for p in classA], [p[1] for p in classA], 'b.')
plt.plot([p[0] for p in classB], [p[1] for p in classB], 'r.')
plt.plot([inputs[i][0] for i in SV if targets[i] == 1], [inputs[i][1] for i in SV if targets[i] == 1], 'b+')
plt.plot([inputs[i][0] for i in SV if targets[i] == -1], [inputs[i][1] for i in SV if targets[i] == -1], 'r+')

xgrid = numpy.linspace(-5, 5)
ygrid = numpy.linspace(-4, 4)

grid = numpy.array([[indicator(x, y) for x in xgrid] for y in ygrid])

plt.contour(xgrid, ygrid, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), linewidths = (1, 3, 1))

plt.axis('equal')
plt.savefig('svmplot.pdf') 
plt.show()