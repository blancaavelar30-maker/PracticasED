class Cadena:
    """Implementación del TAD Cadena"""

    def concatenar(self, cadena1: str, cadena2: str) -> str:
        return cadena1 + cadena2

    def longitud(self, cadena: str) -> int:
        return len(cadena)

    def es_vacia(self, cadena: str) -> bool:
        return cadena == ""

    def son_iguales(self, cadena1: str, cadena2: str) -> bool:
        return cadena1 == cadena2


# Ejecución principal con menú interactivo
if __name__ == "__main__":
    print("Probando el TAD Cadena")
    print("Operaciones: Concatenar, Longitud, Es vacía, Son iguales")

    obj = Cadena()
    opcion = -1  # Inicializamos la variable de control

    while opcion != 0:
        print("\nOperaciones:")
        print("1. Concatenar")
        print("2. Longitud")
        print("3. Es vacía")
        print("4. Son iguales")
        print("0. Salir")

        try:
            opcion = int(input("Elige una opción: "))

            match opcion:
                case 1:
                    print("Ingresa 2 cadenas:")
                    c1 = input("Cadena 1: ")
                    c2 = input("Cadena 2: ")
                    resultado = obj.concatenar(c1, c2)
                    print(f"Concatenación: {resultado}")

                case 2:
                    print("Ingresa una cadena:")
                    c1 = input("Cadena: ")
                    resultado = obj.longitud(c1)
                    print(f"La longitud de '{c1}' es: {resultado}")

                case 3:
                    print("Ingresa una cadena:")
                    c1 = input("Cadena: ")
                    resultado = obj.es_vacia(c1)
                    print(
                        "La cadena está vacía"
                        if resultado
                        else "La cadena NO está vacía"
                    )

                case 4:
                    print("Ingresa 2 cadenas:")
                    c1 = input("Cadena 1: ")
                    c2 = input("Cadena 2: ")
                    resultado = obj.son_iguales(c1, c2)
                    print(
                        "Las cadenas son iguales"
                        if resultado
                        else "Las cadenas son diferentes"
                    )

                case 0:
                    print("¡Adiós!!!")

                case _:
                    print("Opción no válida.")

        except ValueError:
            print("Error: Por favor ingresa un número entero válido.")
