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
x = torch.Tensor(5, 3)
x = torch.rand(5,3)
y= torch.Tensor(3, 10)
y= torch.rand(3,10)
k=x.numpy()
l=y.numpy()
z=k.dot(l)
print(z)
