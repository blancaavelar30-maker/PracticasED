class NaturalCompara:
    """Implementación del TAD Natural para Comparar"""

    def menorIgual(self, numero1: int, numero2: int) -> bool:
        return numero1 <= numero2

    def menor(self, numero1: int, numero2: int) -> bool:
        return numero1 < numero2

    def mayor(self, numero1: int, numero2: int) -> bool:
        return numero1 > numero2

    def mayorIgual(self, numero1: int, numero2: int) -> bool:
        return numero1 >= numero2


# Ejecución principal con menú interactivo
if __name__ == "__main__":
    print("Probando el TAD NaturalCompara")
    print("Valores: 0, 1, 2...")
    print("Operaciones: menorIgual, menor, mayor, mayorIgual")

    obj = NaturalCompara()
    opcion = -1  # Inicializamos la variable de control

    while opcion != 0:
        print("\nOperaciones:")
        print("1. menorIgual")
        print("2. menor")
        print("3. mayor")
        print("4. mayorIgual")
        print("0. Salir")

        try:
            opcion = int(input("Elige una opción: "))

            match opcion:
                case 1:
                    print("Ingresa 2 valores:")
                    n1 = int(input("valor 1: "))
                    n2 = int(input("valor 2: "))
                    resultado = obj.menorIgual(n1, n2)
                    print(f"{n1} <= {n2} : {resultado}")

                case 2:
                    print("Ingresa 2 valores:")
                    n1 = int(input("valor 1: "))
                    n2 = int(input("valor 2: "))
                    resultado = obj.menor(n1, n2)
                    print(f"{n1} < {n2} : {resultado}")

                case 3:
                    print("Ingresa 2 valores:")
                    n1 = int(input("valor 1: "))
                    n2 = int(input("valor 2: "))
                    resultado = obj.mayor(n1, n2)
                    print(f"{n1} > {n2} : {resultado}")

                case 4:
                    print("Ingresa 2 valores:")
                    n1 = int(input("valor 1: "))
                    n2 = int(input("valor 2: "))
                    resultado = obj.mayorIgual(n1, n2)
                    print(f"{n1} >= {n2} : {resultado}")

                case 0:
                    print("¡Adiós!!!")

                case _:
                    print("Opción no válida.")

        except ValueError:
            print("Error: Por favor ingresa un número entero válido.")
