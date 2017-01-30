import torch
import numpy as np
a=np.random.rand(3,5)
b=np.zeros((5,10))
b+=0.1
c=a.dot(b)
print(c)
