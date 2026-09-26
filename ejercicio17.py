class Estudiante:
    """
    Clase que representa a un estudiante.
    Ideal para mostrar cómo nacen los atributos.
    """

    # 1. El Constructor siempre se llama __init__
    # 2. 'self' SIEMPRE es el primer parámetro, seguido de los datos que recibe
    def __init__(self, nombre, matricula):
        # Así se declaran los atributos de la clase (usando self.)
        self.nombre = nombre
        self.matricula = matricula
        self.materias_aprobadas = 0  # Atributo inicializado por defecto

    def aprobar_materia(self):
        # Si olvidamos el 'self.', Python pensará que es una variable local
        # y fallará. Siempre debe llevar self.
        self.materias_aprobadas += 1

    def mostrar_info(self):
        return (
            f"El alumno {self.nombre} ha aprobado {self.materias_aprobadas} materias."
        )


# ================================
# CÓMO USAR LA CLASE (Fuera de la definición)
# ================================
if __name__ == "__main__":
    # 3. Creación del objeto (Instanciación) SIN la palabra 'new'
    alumno1 = Estudiante("Carlos", "19001234")
    alumno2 = Estudiante("Ana", "19005678")

    # Al llamar a los métodos, NO le pasamos el parámetro 'self'.
    # Python lo inyecta de forma invisible por debajo del agua.
    alumno1.aprobar_materia()
    alumno1.aprobar_materia()

    print(alumno1.mostrar_info())
    print(alumno2.mostrar_info())
