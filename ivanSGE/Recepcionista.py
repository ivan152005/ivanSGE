from Empleado import Empleado

class Recepcionista(Empleado):
    def __init__(self):
        super().__init__(nick = "Recepcionista", correo = "recep@gmail.com")
        self.num_consultas = 0