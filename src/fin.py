# Actividad 1: Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, 
# muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, 
# (mas adelante veremos como detectar los fallos usando try y except)

def main():
    contador = 0
    suma_total = 0
    n = ""
    while n != "fin":
        # Entrada
        n = input("Introduzca un numero: ")        
        # Procesamiento
        if n.isdigit():
            contador += 1
            suma_total = suma_total + int(n)
        if not n.isdigit() and n != "fin":
            print("Entrada inválida")
        
        media = suma_total / contador

        # Salida
        if n == "fin":
            print("Cantidad numérica introducida:", contador)
            print("Media de los numeros:", media)
            
        
if __name__ == "__main__":
    main()

    