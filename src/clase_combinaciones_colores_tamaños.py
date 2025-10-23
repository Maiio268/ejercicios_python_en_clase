# Quiero TODAS las combinaciones entre tallas y colores
# SALIDA = 9 combinaciones (3x3)


def mezclar_colores_tallas(colores, tallas):
    for color in colores:
        for talla in tallas:
            
            return color, talla
    
    
def main():
    colores = ['rojo', 'verde', 'azul']
    tallas = ['S', 'M', 'L']
    
    print("Camiseta", color, "talla", talla)
        
    for llamada in range(1, len(colores)):
        color, talla = mezclar_colores_tallas
        print