class Pet:
    def __init__(self,nombre="",altura=0,peso=0,color=""):
        self.nombre=nombre
        self.altura=altura
        self.peso=peso
        self.color=color

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nAltura: {self.altura}\nPeso: {self.peso}\nColor: {self.color}\n"

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color    