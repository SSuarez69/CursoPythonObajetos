from abc import ABC,abstractstaticmethod

class Trabajador():
    @abstractstaticmethod
    def Trabajar(self):
        pass
    
    @abstractstaticmethod
    def Comer(self):
        pass
    
    @abstractstaticmethod
    def dormir(self):
        pass


class Humano():
    def trabajar(self):
        pritnt("El humano esta trabajando")
    
    def comer(self):
        pprit("El Humano esta comiendo")
    
    def dormir(self):
        print("El humano esta durmiendo")


class Robot():
    def trabajar(self):
        pritnt("El Robot esta trabajando")


