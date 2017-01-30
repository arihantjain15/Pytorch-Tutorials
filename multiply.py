# This is a basic tutoril on how to multiply two vectors in PyTorch.
# One of the coolest things in PyTorch is that allows the manipulation of vectors/tensors using numpy subverting Torch's methods.
# This is a cool feature because good old numpy is extremely easy to use! 

import torch
import numpy as np 

# Done using good old numpy
a=np.random.rand(3,5) #initialize a numpy vector 
b=np.zeros((5,10)) # initialize another vector
b+=0.1
c=a.dot(b) # Multiply just as you would in numpy
print(c)


# This can also be done using Torch as follows - 
t = torch.randn(2, 3)
t1 = torch.randn(1, 6)
t2 = torch.randn(6, 1)
torch.addcmul(t, 0.1, t1, t2)
