def validar_password(password: str)-> bool:
    return password == "ilovecoffee"

clave = input("introduce la contraseña:")

if validar_password(clave):
    print("true")
else:
    print("False")