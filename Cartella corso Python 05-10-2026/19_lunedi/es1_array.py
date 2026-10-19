import numpy as np

arr2= np.array([])

arr2 = np.arange(10,50)

arr2 = np.array([], dtype='int64')
print(arr2.dtype)

#convertitore
arr2= arr2.astype('floaat64')
print(arr2.dtype)


#stampa forma
arr2 = np.array([[], []])
print(arr2.shape)



