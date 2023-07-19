class Pet:
    def __init__(self,ID,nombre,peso,altura,descripcion,IDDuenio) :
        self.ID=ID
        self.nombre=nombre
        self.peso=peso
        self.altura=altura
        self.descripcion=descripcion
        self.IDDuenio=IDDuenio

     #seters
    def setID(self,dato):
        self.ID=dato
    def setNombre(self,dato):
        self.nombre=dato
    def setPeso(self,dato):
        self.peso=dato
    def setAltura(self,dato):
        self.altura=dato
    def setDescripcion(self,dato):
        self.descripcion=dato
    def setIDDuenio(self,dato):                    
        self.IDDuenio=dato

    #geters
    def getID(self):
        return self.ID
    def getNombre(self):
        return self.nombre
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura
    def getDescripcion(self):
        return self.descripcion
    def getIDDuenio(self):
        return self.IDDuenio
    
    def __str__(self) -> str:
        return f"\nNombre: {self.nombre}\nPeso: {self.peso}\nAltura: {self.altura}\nDescripcion: {self.descripcion}\nID Dueño: {self.IDDuenio}\nID: {self.ID}"