import numpy as np

def gaussian(X,Y,a,b,sigma,A):
    return A*np.exp(-0.5*((X-a)**2 + (Y-b)**2)/(sigma**2))

