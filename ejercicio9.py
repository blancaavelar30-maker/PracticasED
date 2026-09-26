


def calcular_area_rectangulo(base: float, altura: float) -> float:
    # La variable area se crea en el momento
    area = base * altura
    return area


# Llamada a la funcion
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

resultado = calcular_area_rectangulo(base, altura)
print(f"El area es: {resultado}")

#alcance de variables
impuesto = 0.16 # Variable global 

def calcular_precio_final(precio_base: float) -> float:
    #precio_base es local.
    #Puede LEER la variable global impuesto sin problema.
    return precio_base + (precio_base * impuesto)
resultadoPrecio = calcular_precio_final(500)
print(f"El precio modificado es {resultadoPrecio}")
