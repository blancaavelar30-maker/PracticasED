
def calculadora_basica():

    opcion = -1

    while opcion != 0:

        print("\n--- CALCULADORA BASICA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")

        try:

            opcion = int(input("\nElige una operacion: "))

            match opcion:

                case 1:
                    print("\n-- SUMA --")

                    a = float(input("Ingrese el primer numero: "))
                    b = float(input("Ingrese el segundo numero: "))

                    print(f"Resultado: {a} + {b} = {a + b}")

                case 2:
                    print("\n-- RESTA --")

                    a = float(input("Ingrese el primer numero: "))
                    b = float(input("Ingrese el segundo numero: "))

                    print(f"Resultado: {a} - {b} = {a - b}")

                case 3:
                    print("\n-- MULTIPLICACION --")

                    a = float(input("Ingrese el primer numero: "))
                    b = float(input("Ingrese el segundo numero: "))

                    print(f"Resultado: {a} * {b} = {a * b}")

                case 4:
                    print("\n-- DIVISION --")

                    a = float(input("Ingrese el primer numero: "))
                    b = float(input("Ingrese el segundo numero: "))

                    if b == 0:
                        print("Error matematico: No se puede dividir entre cero")
                    else:
                        print(f"Resultado: {a} / {b} = {a / b}")

                case 0:
                    print("\nSaliendo de la calculadora...")

                case _:
                    print(
                        "Error: opcion no valida. "
                        "Por favor, elige un numero del 0 al 4."
                    )

        except ValueError:

            # Este except atrapa el error si escriben letras en el menu o en los numeros.
            print("Error de formato: Debes ingresar un valor numerico valido.")


calculadora_basica()

