class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        if self.calificacion >= 60:
            return f"{self.nombre} ha aprobado."
        else:
            return f"{self.nombre} no ha aprobado."

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
calificacion = int(input("Ingrese la calificación del estudiante: "))

estudiante1 = Estudiante(nombre, edad, calificacion)

resultado = estudiante1.verificar_aprobacion()

print(resultado)
