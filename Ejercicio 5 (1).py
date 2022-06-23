import numpy as np

array = np.random.randint(0, 100, size=(100, 1)) 
array2 = np.random.randint(0, 100, size=(100, 1)) 
comp = np.sum(array, axis=0)
comp2 = np.sum(array2, axis=0)
sumtol = comp + comp2
print (sumtol)
