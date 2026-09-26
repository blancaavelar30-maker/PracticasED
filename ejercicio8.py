#Crea un ejercicio personal donde utilices las estructuras anteriores.

contraseña_correcta = "ilovecoffee"
intentos = 0

while intentos < 3:

    contraseña = input("Introduzca su contraseña: ")

    if contraseña == contraseña_correcta:

        print("Bienvenido, acceso correcto.")

        materias = int(input("¿Cuántas materias cursó este semestre? "))

        suma = 0

        for i in range(materias):
            calificacion = float(input("Introduzca la calificación: "))
            suma += calificacion

        promedio = suma / materias

        print("Su promedio del semestre es:", promedio)

        if promedio >= 85:
            print("Felicidades, aprobaste el semestre.")
        else:
            print("No aprobaste el semestre.")

        break

    else:

        print("Contraseña incorrecta.")
        intentos += 1

if intentos == 3:
    print("Demasiados intentos fallidos. Acceso denegado.")