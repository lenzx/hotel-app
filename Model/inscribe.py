import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Database.database import DB 

class Inscribe(DB):
    def __init__(self,idRegistro,rutPasajero):
        super().__init__()
        self.__idRegistro = idRegistro
        self.__rutPasajero = rutPasajero
    def getIdRegistro(self):
        return self.__idRegistro
    def getRutPasajero(self):
        return self.__rutPasajero
    
    def verInscribe(self):
        inscripciones = []
        sql = "SELECT * FROM inscribe ORDER BY ID_REGISTRO asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    inscripcion = Inscribe(x[0],x[1])
                    inscripciones.append(inscripcion)
                return inscripciones
            else:
                print("No hay inscripciones registrados")
        except Exception as e:
            print("Error: ", e.args)

    def agregarInscribe(self,inscribe):
        val = (inscribe.getIdRegistro(),inscribe.getRutPasajero())
        sql = "INSERT INTO inscribe (ID_REGISTRO, RUT_PASAJERO) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('la inscripcion a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def modificarInscribe(self,inscipcionNueva,inscripcionActual):
        val = (inscipcionNueva.getIdRegistro(),inscipcionNueva.getRutPasajero(),inscripcionActual.getIdRegistro(),inscripcionActual.getRutPasajero())
        sql = "UPDATE inscribe SET ID_REGISTRO = %s, RUT_PASAJERO = %s  WHERE ID_REGISTRO = %s AND RUT_PASAJERO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)
    
    def quitarInscribe(self,inscripcion):
        val = (inscripcion.getIdRegistro(),inscripcion.getRutPasajero())
        sql = "DELETE FROM inscribe WHERE ID_REGISTRO = %s AND RUT_PASAJERO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('la inscripcion a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)

