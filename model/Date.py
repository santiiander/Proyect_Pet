class Date:
    def __init__(self, asunto="", precio=0, fecha=0, cliente="", mascota=""):
        self.asunto = asunto
        self.precio = precio
        self.fecha = fecha
        self.cliente = cliente
        self.mascota = mascota

    def __str__(self) -> str:
        return f"\nLa sita fue solicitada por:{self.asunto}\nLa Fecha de la misma es el:{self.fecha}\nPrecio:{self.precio}\nLa reserva fue solicitada por:{self.cliente}\nPara:{self.mascota}"

    def get_asunto(self):
        return self.asunto
    def set_asunto(self, asunto):
        self.asunto = asunto
    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio = precio
    def get_fecha(self):
        return self.fecha
    def set_fecha(self, fecha):
        self.fecha = fecha
    def get_cliente(self):
        return self.cliente
    def set_cliente(self, cliente):
        self.cliente = cliente
    def get_mascota(self):
        return self.mascota
    def set_mascota(self, mascota):
        self.mascota = mascota