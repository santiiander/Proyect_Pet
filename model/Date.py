class Date:
    def __init__(self,Duenio,Mascota,Fecha,Presupuesto):
        self.Duenio=Duenio
        self.Mascota=Mascota
        self.Fecha=Fecha
        self.Presupuesto=Presupuesto

    # Setters
    def setDuenio(self, dato):
        self.Duenio = dato
    def setMascota(self, dato):
        self.Mascota = dato
    def setFecha(self, dato):
        self.Fecha = dato
    def setPresupuesto(self, dato):
        self.Presupuesto = dato

    # Getters
    def getDuenio(self):
        return self.Duenio
    def getMascota(self):
        return self.Mascota
    def getFecha(self):
        return self.Fecha
    def getPresupuesto(self):
        return self.Presupuesto
        