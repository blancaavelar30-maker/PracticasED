contraseñacorrecta= "ilovecoffee"
intentos = 0

while intentos < 3:
    contraseña = input("Introdusca su contraseña:")
    if contraseña == contraseñacorrecta:
        print(f"Bienvenido, Su contraseña es correcta. Intentos = {intentos}")
        break
    else:
        print(f"Contraseña incorrecta. Intentos = {intentos}")
        intentos +=1
if intentos==3:
    print("Has agotado el numero de intentos. Acceso denegado")        
