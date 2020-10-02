import numpy as np

l = np.ones((5,5))

u = np.zeros((3,3))

u[1,1] = 9

l[1:-1,1:-1] = u

print(l)