class mainView:
    def menuView(self):
        print("RESERVACION PELUQUERIA CANINA")
        print("1)Realizar reservacion")
        print("2)Ver turnos reservados")
        print("3)Ver usuarios registrados")
        print("4)Descubre nuestros Servicios")
        print("5)Salir")
        print("6) Fechas")
        
    def pedirDNI(self):
        print("Ingrese su DNI para realizar la reservacion.\nEn el caso de que ya se encuentre en nuestra base de datos\nserán autocompletados sus datos: ")

    def despedida(self):
        print("Gracias por usar nuestros servicios A.S")

    def yaRegistrado(self):
        print("Ya se encuentra registrado, procediendo a llenar\nsus datos de forma automatica\nPero quizá necesitemos algunos datos mas")
                    
    def asuntoCita(self):
        print("Ingrese el asunto de la cita a la peluqueria canina")

    def eleccionServicios(self):
        print("Por favor inngrese los servicios a aplicar en la cita para su mascota, 0 para finalizar")

    def printTotal(self):
        print("El precio total de los servicios a su mascota es de: ")    

    def pedirFecha(self):
        print("Ingrese una fecha cercana para su turno, veremos disponibilidad de la misma\n y le notificaremos")

    def cita(self):
        print("A continuacion ingrese el asunto o motivo de la cita")