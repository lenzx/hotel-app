import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Model.costoHabitacion import CostoHabitacion

class CostoHabitacionController:
    def __init__(self):
        self.__costoHabitacion = CostoHabitacion(None,None,None)
    
    def verCostoHabitacion(self):
        return self.__costoHabitacion.verCostoHabitacion()
    
    def modificarCostoHabitacion(self,idCostoHabitacion,idTipoHabitacion,costoBase):
        id_costo_habitacion = idCostoHabitacion
        id_tipo_habitacion = idTipoHabitacion
        costo_base = costoBase
        costo_habitacion =CostoHabitacion(id_costo_habitacion,id_tipo_habitacion,costo_base)
        self.__costoHabitacion.modificarCostoHabitacion(costo_habitacion)

    def agregarCostoHabitacion(self,idCostoHabitacion,idTipoHabitacion,costoBase):
        id_costo_habitacion = idCostoHabitacion
        id_tipo_habitacion = idTipoHabitacion
        costo_base = costoBase
        costo_habitacion =CostoHabitacion(id_costo_habitacion,id_tipo_habitacion,costo_base)
        self.__costoHabitacion.agregarCostoHabitacion(costo_habitacion)

    def eliminarCostoHabitacion(self,id):
        id_costo_habitacion = id
        costo_habitacion = self.__costoHabitacion.verCostoHabitacionId(id_costo_habitacion)
        self.__costoHabitacion.quitarCostoHabitacion(costo_habitacion)
    
