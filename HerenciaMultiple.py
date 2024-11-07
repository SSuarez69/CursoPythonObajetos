# Herencia simple


class Persona:
    def __init__(self, nombre, edad, nancionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nancionalidad = nancionalidad
    
    def hablar(self):
        print("Estas hablando poco ")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return  f"Mi habilidad es: {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(self,nombre,edad,nancionalidad,habilidad,salario,empresa ):
        Persona.__init__(self,nombre,edad,nancionalidad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario
        
    def presentarse(self):
        return f'Hola, soy {self.nombre} y mi habilidad es {self.habilidad}, trabajo en {self.empresa}'
        

roberto = EmpleadoArtista("Roberto",43,"Argentino","Cantar","35000","Programador")

print(roberto.presentarse())

        
