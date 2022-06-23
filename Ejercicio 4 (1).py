import numpy as np


array = np.random.randint(5, 50, size=(15, 12))  
porprom = np.amin(array)

arrsu = np.zeros(shape=5)
for j in range(5):
    suma = sum([fila[j] for fila in array])
    arrsu[j]=(suma)

comp = np.sum(arrsu, axis=0)    
print ("La lista ingresada es la siguiente:")
print (array)
print ()
print("El dato menor de la lista es:")
print (porprom)
print ()
print ("La suma de los valores de las primeras 5 columnas es:")
print (comp)
