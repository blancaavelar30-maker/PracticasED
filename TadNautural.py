class Natural:
    """Implementacion del TAD Natural"""

    def sucesion(self, numero: int) -> int:
        return numero + 1

    def suma(self, numero1: int, numero2: int) -> int:
        return numero1 + numero2

    def producto(self, numero1: int, numero2: int) -> int:
        return numero1 * numero2

    def comparacion(self, numero1: int, numero2: int) -> bool:
        return numero1 == numero2


# Ejecucuion principal con menu interactivo
if __name__ == "__main__":
    print("Probando el TAD Natural")
    print("Valores: 0, 1, 2...")
    print("Operaciones: sucesion, suma, producto y comparacion")

    obj = Natural()
    opcion = -1  # Inicializamos la variable de control

    while opcion != 0:
        print("\nOperaciones:")
        print("1. Sucesion")
        print("2. Suma")
        print("3. Producto")
        print("4. Comparacion")
        print("0. Salir")

        try:
            int(input())
            opcion = int(input("\nElige una opcion"))

            match opcion:
                case 1:
                    print("Ingresa 1 Valor:")
                    n1 = int(input())
                    resultado = obj.sucesion(n1)
                    print(f"la sucesion de {n1 } es {resultado}")

                case 2:
                    print("Ingresa 2 valores:")
                    n1 = int(input("Valor 1:"))
                    n2 = int(input("Valor 2:"))
                    resultado = obj.suma(n1, n2)
                    print(f"La suma de {n1} y {n2}")

                case 3:
                    print("Ingresa 2 valores:")
                    n1 = int(input("Valor 1:"))
                    n2 = int(input("Valor 2:"))
                    resultado = obj.producto(n1, n2)
                    print(f"El producto de {n1} y {n2} es {resultado}")

                case 4:
                    print("Ingresa 2 valores:")
                    n1 = int(input("Valor 1:"))
                    n2 = int(input("Valor 2:"))
                    resultado = obj.comparacion(n1, n2)
                    print(f"La comparacion de {n1} y {n2} es {resultado}")

                case 0:
                    print("Adios!!!")

                case _:  # Equivalente a default
                    print("Opcion no valida ")

        except ValueError:
            print("Error: Por favor ingresa un numero entero valido.")
