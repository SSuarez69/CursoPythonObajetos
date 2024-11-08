import openai

openai.api_base = "api-key"                # Es la clave que genera la pagina de openai
system_rol = ''' Hace de cuenta que son un analizador sentimiento.
                 Yo te paso sentimientos y vos analizas el sentimiento de lo smensajes
                 y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                 SOLO RESPUESTA NUMERICA . Donde -1 es negativa maxima, 0 es nuetral y 1 es positiva maxima.'''
mensajes = [{"role": "system", "content":  system_rol}]

class AnalizadordeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if  polaridad > -0.07 and polaridad <= 0.3:
             return "\x1b[1;31m" + "Negativo" + "\x1b[1;37m"
        elif polaridad > -0.3 and polaridad < 0.1:
           return "\x1b[1;31m" + "Algo negativo"  + "\x1b[1;37m"
        elif polaridad >= 0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral"  + "\x1b[1;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"  + "\x1b[1;37m"
        elif  polaridad > 0.9:
            return "\x1b[1;32m" + "muy positivo"  + "\x1b[1;37m"
        else:
            return "\x1b[1;31m" + "HUY Negativo"  + "\x1b[1;37m"

analizador = AnalizadordeSentimientos()
# resultado = analizador.analizar_sentimiento(0.1)
# print(resultado)

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
    