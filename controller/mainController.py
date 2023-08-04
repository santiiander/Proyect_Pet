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
        self.precioServicios=0
        self.fechas=[]

    def run(self):

        self.consumirClientes()
        servicioInstancia=self.modelService
        servicioInstancia.crearServicios()
        self.llamarFechasSQL()
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
        if chose==6:
            self.printfechas()    


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

    def acumuladorServicios(self):
        chose=9
        self.view.eleccionServicios()
        self.modelService.printearServicios()
        while chose!=0:
            chose=int(input())
            if chose==1:
                self.precioServicios=self.precioServicios+1500
            if chose==2:
                self.precioServicios=self.precioServicios+1000  
            if chose==3:
                self.precioServicios=self.precioServicios+400
            if chose==4:
                self.precioServicios=self.precioServicios+500
            if chose==5:
                self.precioServicios=self.precioServicios+000
            if chose==6:
                self.precioServicios=self.precioServicios+0    
        self.view.printTotal()
        print(self.precioServicios) 
        return self.precioServicios               
    
    def llamarFechasSQL(self):
        #Creamos una clase persona y mascota, en modo peticion
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sanja051/",
        database="Proyect_Pet"
        )
        cursor = conexion.cursor()

        cursor.execute('SELECT fecha FROM Dates')

        registros = cursor.fetchall()

        for i in registros:
            self.fechas.append(i)
        
        conexion.close()

    def printfechas(self):
        for i in self.fechas:
            if len(i) >= 1:  # Verificar que la tupla tenga al menos un elemento
                fecha = i[0]  # Acceder al objeto datetime.date dentro de la tupla
                print(str(fecha.year) + " Año\n" + str(fecha.month) + " Mes\n" + str(fecha.day) + " Dia\n--------------")
            else:
                print("Tupla incorrecta: ", i)


    def seleccionFecha(self):
        self.printfechas()
        self.view.pedirFecha()
        self.fechafinal=str(input())

    def agregar_cita(asunto, precio, fecha, cliente, mascota):
        # Conectarse a la base de datos (asegúrate de cambiar los parámetros de conexión según tu configuración)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sanja051/",
            database="Proyect_Pet"
        )

        # Crear un cursor para ejecutar las consultas
        cursor = connection.cursor()

        # Consulta SQL para insertar una nueva cita en la tabla
        sql = "INSERT INTO Dates (asunto, precio, fecha, cliente, mascota) VALUES (%s, %s, %s, %s, %s)"
        values = (asunto, precio, fecha, cliente, mascota)

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()
        connection.close()


    def crearCita(self):
        self.view.cita()
        asunto=str(input())
        precio=self.acumuladorServicios()
        fecha="2023-07-27"
        cliente=1
        mascota=2
        self.agregar_cita(precio,fecha,cliente,mascota)
