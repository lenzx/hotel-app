import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Model.habitacion import Habitacion

class HabitacionController:
    def __init__(self):
        self.__habitacion = Habitacion(None,None,None,None,None,None)
        
    def agregarHabitacion(self,numeroHabitacion,idTipoHabitacion,capacidadMax,orientacion,min_pasajero):
        n_habitacion = numeroHabitacion
        habitacion_tipo = idTipoHabitacion
        capacidad_max = capacidadMax
        orientacio_hab = orientacion
        capacidad_min = min_pasajero
        habitacion = Habitacion(n_habitacion,habitacion_tipo,capacidad_max,orientacio_hab,capacidad_min,None)
        self.__habitacion.agregarHabitacion(habitacion)

    def eliminarHabitacion(self,numeroHabitacion):
        numero_habitacion = numeroHabitacion
        habitacion = self.__habitacion.verHabitacionId(numero_habitacion)
        habitacion.setHabilitar(0)
        self.__habitacion.modificarHabitacion(habitacion)

    def modificarHabitacion(self,numeroHabitacion, idTipoHabitacion,capacidadMax,orientacion,minPasajero):
        numero_habitacion = numeroHabitacion
        id_tipo_habitacion = idTipoHabitacion
        capacidad_max = capacidadMax
        Orienteacion = orientacion
        min_pasajero = minPasajero
        habitacion = self.__habitacion.verHabitacionId(numero_habitacion)
        habitacion.setIdTipoHabitacion(id_tipo_habitacion)
        habitacion.setCapacidadMax(capacidad_max)
        habitacion.setOrientacion(Orienteacion)
        habitacion.setMinPasajero(min_pasajero)
        self.__habitacion.modificarHabitacion(habitacion)
    def verHabitacion(self):
        return self.__habitacion.verHabitacion()
    def verHabitacionId(self,id):
        habitacion_id = id
        return self.__habitacion.verHabitacionId(habitacion_id)