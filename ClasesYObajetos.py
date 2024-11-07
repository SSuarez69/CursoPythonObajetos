class Celular():
    def __init__(self, marca, modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        print(f"Estas llamado desde un : {self.marca}")
        
    def cortar(self):
        print(f"Cortaste la llamada desde tu : {self.marca}")
    

celular1 = Celular("Samsung", "s23", "89MP")
celular2 = Celular("Nokia", "M3635", "67MP")

print(celular2.marca)

celular1.llamar()
celular2.llamar()

celular1.cortar()
celular2.cortar()