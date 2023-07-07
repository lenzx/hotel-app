import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)

from Database.database import DB 

class TipoHabitacion(DB):
    def __init__(self,idTipoHabitacion,TipoHabitacion):
        super().__init__()
        self.__idTipoHabitacion = idTipoHabitacion
        self.__tipoHabitacion = TipoHabitacion
    
    def getIdTipoHabitacion(self):
        return self.__idTipoHabitacion
    
    def getTipoHabitacion(self):
        return self.__tipoHabitacion
    
    def setIdTipoHabitacion(self,newId):
        self.__idTipoHabitacion = newId
    
    def setTipoHabitacion(self, newNombre):
        self.__tipoHabitacion = newNombre
    
    def agregarTipoHabitacion(self,tipoHabitacion):
        val = (tipoHabitacion.getIdTipoHabitacion(),tipoHabitacion.getTipoHabitacion())
        sql = "INSERT INTO tipo_habitacion (ID_TIPO_HABITACION, TIPO_HABITACION) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
        except Exception as e:
            print("Error: ", e.args)

    def verTipoHabitacion(self):
        tipoHabitaciones = []
        sql = "SELECT * FROM tipo_habitacion ORDER BY ID_TIPO_HABITACION asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    tipoHabitacion = TipoHabitacion(x[0],x[1])
                    tipoHabitaciones.append(tipoHabitacion)
                return tipoHabitaciones
            else:
                print("No hay Tipos de habitaciones registrados")

        except Exception as e:
            print("Error: ", e.args)
    
    def verTipoHabitacionId(self,id):
        val = id
        sql = "SELECT * FROM tipo_habitacion WHERE ID_TIPO_HABITACION = %s "
        try:
            self.cursor.execute(sql,val)
            datos = self.cursor.fetchone()
            if (len(datos) != 0):
                tipo_habitacion = TipoHabitacion(datos[0],datos[1])
                return tipo_habitacion
            else:
                print("No se encontro el tipo habitacion en la base de datos")
        except Exception as e:
            print("Error: ", e.args)

    def modificarTipoHabitacion(self,tipoHabitacion):
        val = (tipoHabitacion.getTipoHabitacion(),tipoHabitacion.getIdTipoHabitacion())
        sql = "UPDATE tipo_habitacion SET TIPO_HABITACION = %s WHERE ID_TIPO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarTipoHabitacion(self,tipoHabitacion):
        val = (tipoHabitacion.getIdTipoHabitacion())
        sql = "DELETE FROM tipo_habitacion WHERE ID_TIPO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el tipo habitacion a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)
