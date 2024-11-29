from sqlalchemy.testing import db_spec

from principal import menu
from principal import menu2
from AirEuropa import AirEuropa
from db import PostgreSQLConnection


if __name__ == '__main__':

    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'root',
        'host': 'localhost',
        'port': '5432',
    }
    db_connection = PostgreSQLConnection(**db_config)

    db_connection.connect()

    menu = menu()
    menu2 = menu2()
    num = 0
    while num != 5:
        try:
            print(menu)
            num = int(input("Ingrese su opción: "))

            match num:
                case 1:
                    vuelos = AirEuropa.mostrar_vuelos(db_connection)
                case 2:
                    direccion = AirEuropa.mostrar_direccion(db_connection)
                case 3:
                    vuelos = AirEuropa.mostrar_vuelos_pasajeros(db_connection)

                case 4:
                    actualizar = AirEuropa.actualizar_vuelos(db_connection)
                case 5:
                    print("Saliendo del programa.")
        except ValueError:
            print("Debe ingresar un número entero.")
