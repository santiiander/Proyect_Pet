class Client:
    clients=[]
    def __init__(self,ID=0,DNI=0,nombre="",apellido="",direccion="",numeroTelef=0,email="",mascota=""):
        self.id=ID
        self.DNI=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.numeroTelef=numeroTelef
        self.email=email
        self.mascota=mascota

    #Metodo To String para llamar a cada persona
    def __str__(self) -> str:
        return f"ID: {self.id}\nDNI: {self.DNI}\nNombre: {self.nombre}\nApellido: {self.apellido}\nDireccion: {self.direccion}\nNumero Telefonico: {self.numeroTelef}\nEmail: {self.email}\nDueño de: {self.mascota}\n--------------------"
    
    #Metodos seters y geters para llamar a los datos o modoficarlos

    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getDNI(self):
        return self.dni
    def getDireccion(self):
        return self.direccion
    def getEmail(self):
        return self.email
    def getNum(self):
        return self.numeroTelef
    def getMascota(self):
        return self.mascota

    def set_nombre(self, dato):
        self.nombre = dato
    def set_apellido(self, dato):
        self.apellido = dato
    def set_dni(self, dato):
        self.dni = dato
    def set_direccion(self, dato):
        self.direccion = dato    
    def set_num_telefono(self, dato):
        self.numeroTelef = dato
    def set_mascota(self, dato):
        self.mascota = dato
    



