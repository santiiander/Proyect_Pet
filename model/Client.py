class Client:
    def __init__(self,ID,DNI,nombre,apellido,direccion,celular,IDmascosta):
        self.ID=ID
        self.DNI=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.celular=celular
        self.IDmascota=IDmascosta

    #definimos los seters 

    def setDNI(self,dato):
        self.DNI=dato
    def setNombre(self,dato):
        self.nombre=dato
    def setApellido(self,dato):
        self.apellido=dato
    def setDireccion(self,dato):
        self.direccion=dato
    def setCelular(self,dato):
        self.celular=dato
    def setIDMascosta(self,dato):
        self.IDmascota=dato       

    #definimos los geters

    def getID(self):
        return self.ID
    def getDNI(self):
        return self.DNI
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getDireccion(self):
        return self.direccion
    def getCelular(self):
        return self.direccion
    def getMascotaID(self):
        return self.IDmascota
    
    def __str__(self) -> str:
        return f"\nNombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nDireccion: {self.direccion}\nCelular: {self.celular}\nID: {self.ID}"
    
Santiago=Client(1,44297673,"Santiago","Andermatten","Avenida Universidad 192",3472468850,1)
print(Santiago)