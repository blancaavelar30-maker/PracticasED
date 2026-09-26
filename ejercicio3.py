calificacion = int(input("Intoduce tu calificacion:"))

if calificacion == 100:
    print("¡Calificacion perfecta!")
elif calificacion >= 70:
    # se ejecuta si la condicion del "if" fue falsa, pero esta en verdadera
    print ("Aprovado")
else:
    #se ejecuta si ninguna de las condiciones anteriores fue verdadera 
    print("Reprobado")