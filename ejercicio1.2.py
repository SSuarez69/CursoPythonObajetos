class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando ....")


nombre = input("Digame su nombre : ")
edad = input("Ahora su edad : ")
grado = input("Por uñtimo, su grado : ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE : \n \n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Edad: {estudiante.grado} \n
      
      """)

estudiar = input()

if(estudiar.lower() == "estudiar"):
    estudiante.estudiar()

