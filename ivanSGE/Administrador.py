from Empleado import Empleado

class Administrador(Empleado):
    def __init__(self):
        super().__init__(nick = "Admin", correo = "admin@admin.com")
        self.num_actualizaciones = 0