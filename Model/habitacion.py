import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Database.database import DB

class Habitacion(DB):
    def __init__(self,NumeroHabitacion,IdTipoHabitacion,CapacidadMax,Orientacion,MinPasajero,Habilitar=1):
        super().__init__()
        self.__numeroHabitacion = NumeroHabitacion
        self.__idTipoHabitacion = IdTipoHabitacion
        self.__capacidadMax = CapacidadMax
        self.__orientacion = Orientacion
        self.__minPasajero = MinPasajero
        self.__habilitar = Habilitar
    
    def getNumeroHabitacion(self):
        return self.__numeroHabitacion
    def getIdTipoHabitacion(self):
        return self.__idTipoHabitacion
    def getCapacidadMax(self):
        return self.__capacidadMax
    def getOrientacion(self):
        return self.__orientacion
    def getMinPasajero(self):
        return self.__minPasajero
    def getHabilitar(self):
        return self.__habilitar
    def setNumeroHasbitacion(self,new_numeroHabitacion):
        self.__numeroHabitacion = new_numeroHabitacion
    def setIdTipoHabitacion(self,new_idTipoHabitacion):
        self.__idTipoHabitacion = new_idTipoHabitacion
    def setCapacidadMax(self,new_capacidadMax):
        self.__capacidadMax = new_capacidadMax
    def setOrientacion(self,new_orientacion):
        self.__orientacion = new_orientacion
    def setMinPasajero(self,new_minPasajero):
        self.__minPasajero = new_minPasajero
    def setHabilitar(self, new_habilitar):
        self.__habilitar = new_habilitar
    
    

    def verHabitacion(self):
        habitaciones = []
        sql = "SELECT * FROM habitacion WHERE habilitar = 1 ORDER BY N_HABITACION asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    habitacion = Habitacion(x[0],x[1],x[2],x[3],x[4],x[5])
                    habitaciones.append(habitacion)
                return habitaciones
            else:
                print("No hay habitacion en la base de datos")
        except Exception as e:
            print("Error: ", e.args)

    def verHabitacionId(self,id):
        val = id
        sql = "SELECT * FROM habitacion WHERE N_HABITACION = %s "
        try:
            self.cursor.execute(sql,val)
            datos = self.cursor.fetchone()
            if (len(datos) != 0):
                habitacion = Habitacion(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
                return habitacion
            else:
                print("No se encontro la habitacion en la base de datos")
        except Exception as e:
            print("Error: ", e.args)

    def agregarHabitacion(self,habitacion):
        val = (habitacion.getNumeroHabitacion(),habitacion.getIdTipoHabitacion(),habitacion.getCapacidadMax(),habitacion.getOrientacion(),habitacion.getMinPasajero())
        sql = "INSERT INTO habitacion (N_HABITACION, ID_TIPO_HABITACION,CAPACIDAD_MAX,ORIENTACION,MIN_PASAJERO) VALUES (%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('habitacion agregada')
        except Exception as e:
            print("Error: ", e.args)

    def modificarHabitacion(self,habitacion):
        val = (habitacion.getIdTipoHabitacion(),habitacion.getCapacidadMax(),habitacion.getOrientacion(),habitacion.getMinPasajero(),habitacion.getHabilitar(),habitacion.getNumeroHabitacion())
        sql = "UPDATE habitacion SET ID_TIPO_HABITACION = %s, CAPACIDAD_MAX = %s, ORIENTACION = %s, MIN_PASAJERO = %s, HABILITAR = %s WHERE N_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarHabitacion(self,habitacion):
        val = (habitacion.getNumeroHabitacion())
        sql = "DELETE FROM habitacion WHERE N_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('la habitacion a sido eliminada')
        except Exception as e:
            print("Error: ", e.args)