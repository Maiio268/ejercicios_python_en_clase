# Programa pregunta un numero (n), que indica el numero de lineas y asteriscos en la ultima linea, yendo desde 1 hasta n ascendentemente
# EJEMPLO: 
'''
ENTRADA: 5
SALIDA:
*
**
***
****
*****
'''
n = int(input("Dime el tamaño: "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("\n")



