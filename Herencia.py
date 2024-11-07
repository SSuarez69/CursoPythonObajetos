# Herencia simple

class Persona:
    def __init__(self, nombre, edad, nancionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nancionalidad = nancionalidad
    
    def hablar(self):
        print("Estas hablando poco ")
        

class Empleado(Persona):
    def __init__(self,nombre,edad,nancionalidad, trabajo, salario):
        super().__init__(nombre,edad,nancionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
roberto = Empleado("Roberto", "34", "argentino", "Programador", "459900")

roberto.hablar()
            
        
