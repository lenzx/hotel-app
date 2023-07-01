import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from datetime import datetime
from datetime import timedelta
from Database.database import DB 

class Registro(DB):
    def __init__(self,idRegistro,nHabitacion,rutPasajeroResponsable,fechaAsignacion,fechaFin,nPersonas,costoAdicionalPersona,costoTotal):
        super().__init__()
        self.__idRegistro = idRegistro
        self.__nHabitacion = nHabitacion
        self.__rutPasajeroResponsable = rutPasajeroResponsable
        self.__fechaAsignacion = fechaAsignacion
        self.__fechaFin = fechaFin
        self.__nPersonas = nPersonas
        self.__costoAdicionalPersona = costoAdicionalPersona
        self.__costoTotal = costoTotal

    def getIdRegistro(self):
        return self.__idRegistro
    def getNumeroHabitacion(self):
        return self.__nHabitacion
    def getRutPasajeroResponsable(self):
        return self.__rutPasajeroResponsable
    def getFechaAsignacion(self):
        return self.__fechaAsignacion
    def getFechaFin(self):
        return self.__fechaFin
    def getNumeroPersonas(self):
        return self.__nPersonas
    def getCostoAdicionalPorPersona(self):
        return self.__costoAdicionalPersona
    def getCostoTotal(self):
        return self.__costoTotal

    def verRegistro(self):
        registros = []
        sql = "SELECT * FROM registro ORDER BY ID_REGISTRO asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    registro = Registro(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
                    registros.append(registro)
                return registros
            else:
                print("No hay registros en la base de datos")

        except Exception as e:
            print("Error: ", e.args)

    def agregarRegistro(self,registro):
        val = (registro.getNumeroHabitacion(),registro.getRutPasajeroResponsable(),registro.getFechaAsignacion(),registro.getFechaFin(),registro.getNumeroPersonas(),registro.getCostoAdicionalPorPersona(),registro.getCostoTotal())
        sql = "INSERT INTO registro (N_HABITACION, RUT_PASAJERO_RESPONSABLE, FECHA_ASIGNACION, FECHA_FIN, N_PERSONAS, COSTO_ADICIONAL_PERSONA, COSTO_TOTAL) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('Registro agregada')
        except Exception as e:
            print("Error: ", e.args)

    def ModificarRegistro(self,registro):
        val = (registro.getNumeroHabitacion(),registro.getRutPasajeroResponsable(),registro.getFechaAsignacion(),registro.getFechaFin(),registro.getNumeroPersonas(),registro.getCostoAdicionalPorPersona(),registro.getCostoTotal(),registro.getIdRegistro())
        sql = "UPDATE registro SET N_HABITACION = %s, RUT_PASAJERO_RESPONSABLE = %s, FECHA_ASIGNACION = %s, FECHA_FIN = %s, N_PERSONAS = %s , COSTO_ADICIONAL_PERSONA = %s, COSTO_TOTAL = %s WHERE ID_REGISTRO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarRegistro(self,registro):
        val = (registro.getIdRegistro())
        sql = "DELETE FROM registro WHERE ID_REGISTRO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el registro a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)
