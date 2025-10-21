# Se introduce una cadena y devuelve una cadena SOLO con las vocales de la cadena introducida.
def procesar_vocales(frase):
    frase_nueva = ""
    for letra in frase:
        if letra in "aeiouAEIOU":
            frase_nueva += letra
    return frase_nueva
def main():
    frase = input("Introduce una frase: ")
    resultado = procesar_vocales(frase)
    print("Frase modificada con vocales:", resultado)


if __name__ == "__main__":
    main()