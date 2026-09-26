try:
    #Codigo que podria fallar
    edad = int(input("Ingresa su edad en numeros:"))
    print(f"tines{edad} años.")
except ValueError:
    # Se ejecuta solo si el usuario teclea texto en lugar de un numero 
    print("Error: Debes ingresar un numero entero valido.")    

    # Capturar mensaje de error original 
    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print(f"Ocurrio un error matematico: {e}")

# Multiples excepciones
lista_numeros = [10, 20, 30]
def procesar_datos(indice):
    try:
        #podria fallar si el indice no existe oh si dividimos por cero 
        valor = lista_numeros[indice]
        calculo = 100 / valor
        print(f"El resultado es {calculo}")

    except IndexError:
        print("Error: El idice que buscas esta fuera de los limites del arreglo.")
    except ZeroDivisionError:
        print ("Error: El valor en esa posicion es 0, no se puede dividir.")
    except Exception as e:
        #el bloque general de Exception siempre debe ir al final (como un default)
        print(f"Ocurrio un error inesperado:{e}")


print(f"Datos del arreglo{lista_numeros}")
indice = int(input("Tecle un indice para ver los datos de esa posicion"))
procesar_datos(indice)

try:
    archivo = open("datos_estudiantes.txt", "r")
    #intentamos leer el archivo...
    print(archivo.read())

except FileNotFoundError:
    print("El archivo no existe en la carpeta.")

else:
    # Esto corre solo si el archivo se abrio correctamente 
    print("Lectura exitosa, procesando datos...")

finally:
    #Esto corre pase lo que pase (haya existido el archivo o no, falle o no
    print("Termino el bloque de ejecucion.")
    archivo.close()