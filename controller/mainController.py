from model.Client import Client
from model.Pet import Pet
from model.Date import Date
from model.Service import Service

from view.mainView import mainView
import mysql.connector
#Controlador dedicado a crear una persona y una mascota para la Cita
class mainController:
    def __init__(self,modelClient=Client(),modelMascota=Pet(),modelDate=Date(),modelService=Service(),view=mainView()):
        self.modelClient=modelClient
        self.modelMascota=modelMascota
        self.modelDate=modelDate
        self.modelService=modelService
        self.view=view
        #self.clientes=[]

    def run(self):

        self.consumirClientes()
        servicioInstancia=self.modelService
        servicioInstancia.crearServicios()
        self.view.menuView()
        chose=int(input())
        if chose==1:
            self.crearCita()
        if chose==2:
            pass
        if chose==3:
            self.printearReservaciones()
        if chose==4:
            servicioInstancia.printearServicios()
        if chose==5:
            self.view.despedida()
            exit()    


    def consumirClientes(self):
        #Creamos una clase persona y mascota, en modo peticion
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sanja051/",
        database="Proyect_Pet"
        )
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM Clients')

        registros = cursor.fetchall()

        for i in registros:
            user=Client(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
            self.modelClient.clients.append(user)  # Agregar la instancia del cliente a la lista
        
        conexion.close()

    def printearReservaciones(self):
        for cita in self.modelClient.clients:
            print(cita)    

    def crearCita(self):
        self.view.pedirDNI()
        dato= int(input())
        for client in self.modelClient.clients:
            if int(client.DNI)==int(dato):
                self.view.yaRegistrado()
                self.view.asuntoCita()
                cita=str(input())
                Date()