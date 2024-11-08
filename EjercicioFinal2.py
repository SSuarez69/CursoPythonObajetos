import openai

openai.api_base = "api-key"                # Es la clave que genera la pagina de openai
system_rol = ''' Hace de cuenta que son un analizador sentimiento.
                 Yo te paso sentimientos y vos analizas el sentimiento de lo smensajes
                 y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                 SOLO RESPUESTA NUMERICA . Donde -1 es negativa maxima, 0 es nuetral y 1 es positiva maxima.'''
mensajes = [{"role": "system", "content":  system_rol}]


class Sentimientos():
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str_(self):
        return "\x1b[1;{}m{}\x1b[1;37m".format(self.color,self.nombre)

class AnalizadordeSentimientos:
    def __init__(self,rangos):
        self.rangos =  rangos
    
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]: 
                return sentimiento
        
        return sentimiento("Muy negativo", "31")
    
rangos= [
    ((-0.6,-0.3),Sentimientos("Negativo","31")),
    ((-0.3,-0.1),Sentimientos("Algo Negativo","31")),
    ((-0.1,0.1),Sentimientos("Neultral","331")),
    ((0.1,0.4),Sentimientos("Algo Pisitivo","32")),
    ((0.4,0.9),Sentimientos("Positivo","32")),
    ((0.9,1),Sentimientos("My positivo","32"))
]

analizador = AnalizadordeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" + "Ingresame algo!"  + "\x1b[1;37m")
    mensajes.append({"role": "user","content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        menssages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message["content"]
    
    mensajes.append({"role": "assistant", "content": respuesta })
    
    sentimientios = analizador.analizar_sentimiento(float(respuesta))
    
    print(sentimientios)
    