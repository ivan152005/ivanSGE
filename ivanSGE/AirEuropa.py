from Log import Log
import Constantes as consulta
import pandas as pd
from sqlalchemy import text
from Empleados import Empleados

class AirEuropa:

    @staticmethod
    def mostrar_vuelos(conexion):
        id_cliente = int(input("\nIntroduce el ID del cliente: "))

        try:
            try:
                query = text(consulta.query1_1)
                print(query)
                result = conexion.execute_query(query, {'id': id_cliente})
                if not result:
                    print("No se ha encontrado al cliente\n")
                    Log.log(f"CONSULTAR VUELOS DE CLIENTE", level="ERROR")
                else:
                    df = pd.DataFrame(result)
                    print(f"VUELOS DE CLIENTE ID: {id_cliente}:\n")
                    print(df)
                    Log.log(f"CONSULTAR VUELOS DE CLIENTE", level="INFO")
            except Exception as e:
                print("Error, no hay conexion o el id es inválido\n")
                Log.log(f"CONSULTAR VUELOS DE CLIENTE", level="ERROR")

        except Exception as e:
            print(f"Error al mostrar los vuelos: {e}")
            Log.log(f"CONSULTAR CLIENTES", level="ERROR")

    @staticmethod
    def mostrar_direccion(conexion):
        id_cliente = int(input("\nIntroduce el ID del cliente: "))

        try:
            try:
                query = text(consulta.query2)
                result = conexion.execute_query(query, {'id': id_cliente})
                if not result:
                    print("No se ha encontrado al cliente\n")
                    Log.log(f"CONSULTAR DIRECCION DE CLIENTE", level="ERROR")
                else:
                    print(f"DIRECCION DE CLIENTE ID: {id_cliente}:\n")
                    print(result)
                    Log.log(f"CONSULTAR DIRECCION DE CLIENTE", level="INFO")
            except Exception as e:
                print("Error, no hay conexion o el id es inválido\n")
                Log.log(f"CONSULTAR DIRECCION DE CLIENTE", level="ERROR")

        except Exception as e:
            print(f"Error al mostrar los vuelos: {e}")
            Log.log(f"CONSULTAR DIRECCION", level="ERROR")

    @staticmethod
    def mostrar_vuelos_pasajeros(conexion):
        try:
            query = text(consulta.query1)
            result = conexion.execute_query(query)
            if not result:
                print("No se han encontrado vuelos\n")
                Log.log(f"CONSULTAR VUELOS", level="ERROR")
            else:
                df = pd.DataFrame(result)
                print(f"Vuelos:\n")
                print(df)
                Log.log(f"CONSULTAR VUELOS", level="INFO")
        except Exception as e:
            print("Error, no hay conexion o el id es inválido\n")
            Log.log(f"CONSULTAR VUELOS", level="ERROR")


    @staticmethod
    def actualizar_vuelos(conexion):
        try:
            query = text(consulta.query4)
            result = conexion.execute_query(query)
            if not result:
                print("No se han encontrado vuelos\n")
            else:
                print(f"Vuelos actualizados:\n")
                Log.log(f"ACTUALIZAR VUELOS", level="INFO")
        except Exception as e:
            print("Error, no hay conexion o el id es inválido\n")
            Log.log(f"ACTUALIZAR VUELOS", level="ERROR")