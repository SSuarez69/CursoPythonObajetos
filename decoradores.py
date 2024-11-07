def decorador(funcion):
    def funcion_modificada():
        print("Antes de la llamada a la funcion")
        funcion()
        print("Desupes del llamado a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola dalton como andas ?")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola dalton como andas ?")
    
saludo()
    
