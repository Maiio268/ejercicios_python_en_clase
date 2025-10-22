'''
La entrada consiste en una serie de horas, cada una en una línea. Cada hora está formada por las horas y los minutos 
separados por : y utilizando siempre dos dígitos. 
'''
# Se utiliza una representación en formato 24 horas (es decir, desde 00:00 a 23:59).
# La entrada termina cuando la hora es la medianoche (00:00), que no debe procesarse.

def pedir_datos():
    '''
    Pide la hora
    '''
    hora = input("Introduce una hora en formato 24 horas (HH:MM): ")
    return hora

def transforma_hora(hora):
    '''
    Transforma la hora en formato HH:MM en horas y minutos por separado
    '''
    partes_hora = hora.split(":")
    horas = int(partes_hora[0])
    minutos = int(partes_hora[1])

    minutos_totales = (24-horas)*60 + (60-minutos)
    return minutos_totales
    
def mostrar_resultado(minutos_totales):
    print("Minutos que faltan para medianoche:", minutos_totales)

def main():
    hora = pedir_datos()
    while hora != "00:00":

        minutos_totales = transforma_hora(hora)

        mostrar_resultado(minutos_totales)

        hora = pedir_datos() 

if __name__ == "__main__":
    main()

