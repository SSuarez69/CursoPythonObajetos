class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
       del self.__nombre 
   
        

dalto = Persona("Lucas", 21)

nombre = dalto.nombre

dalto.nombre = "sasasa"



print(nombre)
print(dalto.nombre)

del dalto.nombre