# Se introduce una cadena y devuelve una cadena SOLO con las vocales de la cadena introducida.
def saca_vocales(frase:str) -> str:
    frase_nueva = ""
    for letra in frase.lower():
        if letra in "aeiou":
            frase_nueva += letra
    return frase_nueva

def main():
    frase = input("Introduce una frase: ")
    resultado = saca_vocales(frase)
    print("Frase modificada con vocales:", resultado)

if __name__ == "__main__":
    main()