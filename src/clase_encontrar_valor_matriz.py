# Pedir un valor y encontrar ese valor en la matriz, indicar si se encuentra o no, y si se encuentra indicar en que fila y columna
numero = int(input("Valor a encontrar: "))

matriz = [(1, 2, 3),
          (4, 5, 6),
          (7, 8, 9)]

for i in len(matriz):
    for j in matriz(i):
        if matriz[i][j] == numero:
            print("Numero", numero, "encontrado en fila:", i, "y columna:", j)
        else:
            print("Numero no encontrado")


