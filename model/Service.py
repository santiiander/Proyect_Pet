class Service:
    services=[]
    def __init__(self,nombre="",precio=0):
        self.nombre=nombre
        self.precio=precio

    def __str__(self):
        return f"\nNombre del Servicio: {self.nombre}\nPrecio del Servicio: {self.precio}"

    def getnombre(self):
        return self.nombre

    def setnombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def getprecio(self):
        return self.precio

    def setprecio(self, nuevo_precio):
        self.precio = nuevo_precio

    def crearServicios(self):
        CortePelo=Service("Corte de pelo",1500)
        self.services.append(CortePelo)
        Banio=Service("Baño",1000)
        self.services.append(Banio)
        Perfume=Service("Perfumado",400)
        self.services.append(Perfume)
        Unias=Service("Corte de uñas",500)
        self.services.append(Unias)
        Transporte=Service("Traslado de tu mascota\nIda y vuelta",1000)
        self.services.append(Transporte)
        Vacunas=Service("Vacunas - Proximamente",0)
        self.services.append(Vacunas)

    def printearServicios(self):
        for service in self.services:
            print(service)
"""
# Crear una instancia de Service
service_instance = Service()

# Llamar al método crearServicios()
service_instance.crearServicios()

# Llamar al método printearServicios()
service_instance.printearServicios()
"""