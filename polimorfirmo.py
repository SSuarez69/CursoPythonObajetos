class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def  Hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
print(gato.sonido())

perro = Perro()
print(perro.sonido())

Hacer_sonido(gato)