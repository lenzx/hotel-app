import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Database.database import DB 

class CostoHabitacion(DB):
    def  __init__(self,idCostoHabitacion,idTipoHabitacion,costoBase):
        super().__init__()
        self.__idCostoHabitacion = idCostoHabitacion
        self.__idTipoHabitacion = idTipoHabitacion
        self.__costoBase = costoBase
    
    def getIdCostoHabitacion(self):
        return self.__idCostoHabitacion
    
    def getIdTipoHabitacion(self):
        return self.__idTipoHabitacion
    
    def getCostoBase(self):
        return self.__costoBase

    def agregarCostoHabitacion(self,costoHabitacion):
        val = (costoHabitacion.getIdCostoHabitacion(),costoHabitacion.getIdTipoHabitacion(),costoHabitacion.getCostoBase())
        sql = "INSERT INTO costo_habitacion (ID_COSTO_HABITACION, ID_TIPO_HABITACION,COSTO_BASE) VALUES (%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el costo de habitacion a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarCostoHabitacion(self,costoHabitacion):
        val = costoHabitacion.getIdCostoHabitacion()
        sql = "DELETE FROM costo_habitacion WHERE ID_COSTO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el costo habitacion a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)
    
    def modificarCostoHabitacion(self,costoHabitacion):
        val = (costoHabitacion.getIdTipoHabitacion(),costoHabitacion.getCostoBase(),costoHabitacion.getIdCostoHabitacion())
        sql = "UPDATE costo_habitacion SET ID_TIPO_HABITACION = %s , COSTO_BASE = %s  WHERE ID_COSTO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def verCostoHabitacion(self):
        costoHabitaciones = []
        sql = "SELECT * FROM costo_habitacion ORDER BY ID_COSTO_HABITACION asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    costoHabitacion = CostoHabitacion(x[0],x[1],x[2])
                    costoHabitaciones.append(costoHabitacion)
                return costoHabitaciones
            else:
                print("No hay costos asignados")
        except Exception as e:
            print("Error: ", e.args)
