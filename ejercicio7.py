materias = int(input("¿Cuantas materias cursaste este semestre?:"))
suma = 0
for i in range(materias):
    calificacion=float(input(f"Introducela calificacion de la materia {i+1}:"))
    suma+=calificacion
    promedio= suma/materias
print(f"Tu promedio es:{promedio}")

if promedio >= 85:
    print("¡Felicidades!Eres apto para la beca.")
else:
    print("No alcanzaste el promedio requerido para la beca.")
    