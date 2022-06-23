import time
import pandas as pd
n = int(input("Ingrese el numero de Filas (alumnos): "))
df = pd.DataFrame(columns=['Nombre', 'Edad'],
                  index=range(n))

print ("Para el llenado de esta tabla primero ingrese los nombres, posteriormente se le pedira la edad en los lugares de terminacion 1 por ejemplo x0,1")
time.sleep(3)
for i in range(n):
    t = str(i)
    for k in range (2):
        q = str(k)
        x = input("Ingrese el valor de x"+ t + "," + q + ": ")
        df.iloc[i,k] = (x)

porprom = df.sort_values('Edad',ascending=False)
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (df)
print()
print("El alumno con mayor edad es:")
print(arx)