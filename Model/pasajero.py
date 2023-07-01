import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)

from Database.database import DB 

class Pasajero(DB):
    def __init__(self,rutPasajero,nombre):
        super().__init__()
        self.__rutPasajero = rutPasajero
        self.__nombre = nombre

    def getRut(self):
        return self.__rutPasajero
    
    def getNombre(self):
        return self.__nombre
    
    def agregarPasajero(self,pasajero):
        val = (pasajero.getRut(),pasajero.getNombre())
        sql = "INSERT INTO pasajero (RUT_PASAJERO, NOMBRE) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el pasajero a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarPasajero(self,pasajero):
        val = (pasajero.getRut())
        sql = "DELETE FROM pasajero WHERE RUT_PASAJERO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el pasajero a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)

    def modificarPasajero(self,pasajero):
        val = (pasajero.getNombre(),pasajero.getRut())
        sql = "UPDATE pasajero SET NOMBRE = %s WHERE RUT_PASAJERO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def verPasajero(self):
        pasajeros = []
        sql = "SELECT * FROM pasajero ORDER BY RUT_PASAJERO asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    pasajero = Pasajero(x[0],x[1])
                    pasajeros.append(pasajero)
                return pasajeros
            else:
                print("No hay pasajeros registrados")

        except Exception as e:
            print("Error: ", e.args)