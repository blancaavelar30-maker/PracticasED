def banco():
    saldo = 10000
    opcion = -1
    while opcion != 0:
        print("\n--- BANCO ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("0. Salir")
        try:
            opcion = int(input("Elige una opción: "))
            match opcion:
                case 1:
                    print(f"\nTu saldo actual es: ${saldo}")
                case 2:
                    cantidad = float(input("Ingresa la cantidad a depositar: "))
                    saldo += cantidad
                    print(f"Depósito exitoso. Tu nuevo saldo es: ${saldo}")
                case 3:
                    cantidad = float(input("Ingresa la cantidad a retirar: "))
                    if cantidad > saldo:
                        print("Error: Saldo insuficiente.")
                    else:
                        saldo -= cantidad
                        print(f"Retiro exitoso. Tu nuevo saldo es: ${saldo}")
                case 0:
                    print("Saliendo del banco...")
                case _:
                    print(
                        "Error: Opción no válida. Por favor, elige un número del 0 al 3."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numérico válido.")


banco()
