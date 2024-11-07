
class TandqueCombustible():
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.cantidad += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usuar_combustible(self,cantidad):
        self.combustible -= cantidad 
    

        

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2 :
            self.posicion += distancia
            self.tanque.usuar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
        
    def obtener_posicion(self):
        return self.posicion
    

tanque = TandqueCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
print(autito.mover(10))
print(autito.obtener_posicion())
print(autito.mover(30))
print(autito.obtener_posicion())
print(autito.mover(55))
print(autito.obtener_posicion())
print(autito.mover(70))
print(autito.obtener_posicion())
print(autito.mover(70))
print(autito.obtener_posicion())