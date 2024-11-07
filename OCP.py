class Notificador():
    def __init__(self,usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Mensaje enviado por Email: {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Mensaje enviado por SMS:{self.sms}")

        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Mensaje enviado por Whatssap:{self.whatssap}")

        
    