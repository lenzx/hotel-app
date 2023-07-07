import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Model.tipoHabitacion import TipoHabitacion

class TipoHabitacionController:
    def __init__(self):
        self.__tipoHabitacion = TipoHabitacion(None,None)

    def verTipoHabitacion(self):
        return self.__tipoHabitacion.verTipoHabitacion()
    
    def verTipoHabitacionId(self,id):
        tipo_habitacion_id = id
        return self.__tipoHabitacion.verTipoHabitacionId(tipo_habitacion_id)
    
    def agregarTipoHabitacion(self,idTipoHabitacion,nombreTipoHabitacion):
        id_tipo_habitacion = idTipoHabitacion
        nombre_tipo_habitacion = nombreTipoHabitacion
        tipo_habitacion = TipoHabitacion(id_tipo_habitacion,nombre_tipo_habitacion)
        self.__tipoHabitacion.agregarTipoHabitacion(tipo_habitacion)

    def modificarTipoHabitacion(self,id,nombre_habitacion):
        tipo_habitacion_id = id
        tipo_habitacion = self.__tipoHabitacion.verTipoHabitacionId(tipo_habitacion_id)
        nuevo_nombre = nombre_habitacion
        tipo_habitacion.setTipoHabitacion(nuevo_nombre)
        self.__tipoHabitacion.modificarTipoHabitacion(tipo_habitacion)

    def eliminarTipoHabitacion(self,id):
        tipo_habitacion_id = id
        tipo_habitacion = self.__tipoHabitacion.verTipoHabitacionId(tipo_habitacion_id)
        self.__tipoHabitacion.quitarTipoHabitacion(tipo_habitacion)

