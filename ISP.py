from abc import ABC,abstractstaticmethod

class Trabajador():
    @abstractstaticmethod
    def Trabajar(self):
        pass

class comendor():
    @abstractstaticmethod
    def Comer(self):
        pass

class dormidor():
    @abstractstaticmethod
    def dormir(self):
        pass


class Humano(Trabajador,comendor,dormidor):
    def trabajar(self):
        print("El humano esta trabajando")
    
    def comer(self):
        print("El Humano esta comiendo")
    
    def dormir(self):
        print("El humano esta durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El Robot esta trabajando")


trabajador = Humano()
trabajador.trabajar()

robot = Robot()
robot.trabajar()