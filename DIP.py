# class Diccionario():
#     def verificar_Palabra(self,palabra):
#         #logica para verificar palabras
#         pass

# class CorrectorOrtografico():
#     def __init__(self):
#         self.diccionario = Diccionario()
    
#     def corregir_palabras(self,text):
#         #pasamos el diccionario para corregir palabras
#         pass

from abc import ABC, abstractstaticmethod

class VerificadorOrtografico():
    @abstractstaticmethod
    def verificar_Palabra(self,palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_Palabra(self,palabra):
         #logica para verificar palabras
         pass

class CorrectorOrtografico():
    def __init__(self, verificadror):
        self.verificador = verificadror
    
    def Corregir_texto(self):
       #Usamor el verificro para corregir texto
       pass
  
   corrector = CorrectorOrtografico(Diccionario())
   