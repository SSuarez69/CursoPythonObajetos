class Auto():
    def __init__(self):
        self.estado = "apagado"
    
    def encender(self):
        self.estado = "encendido"
    
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("Conduciendo...")

mi_auto = Auto()
mi_auto.conducir()