from Empleados import Empleados
from Recepcionista import Recepcionista
from Administrador import Administrador

def menu():

    empleados = Empleados()
    #añadir aqui a los empleados el admin y el recepcionista
    #cada vez que se realice una actualización o una consulta se deberá sumar 1.

    # para que solo los ñaada una vez
    if len(empleados.empleados) == 0:
        empleados.empleados.append(Administrador)
        empleados.empleados.append(Recepcionista)

    print("\n--- MENÚ ---")
    print("1. Mostrar los vuelos de un cliente")
    print("2. Mostrar la dirección de un usuario")
    print("3. Vuelo de los pasajeros")
    print("4. Actualización de muertos")
    print("5. Salir")


def menu2():
    print("\n--- MENÚ ---")
    print("1. Buscar por billete mas caro")
    print("2. Por billete mas barato")
    print("3. Media del precio billetes")