import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Model.pasajero import Pasajero

class PasajeroController:
    def __init__(self) -> None:
        self.__pasajero = Pasajero(None,None)
    
    def agregarPasajero(self,rut,nombre):
        rut_pasajero = rut
        nombre_pasajero = nombre
        pasajero = Pasajero(rut_pasajero,nombre_pasajero)
        self.__pasajero.agregarPasajero(pasajero)
    
    def eliminarPasajero(self,rut):
        rut_pasajero = rut
        pasajero = Pasajero(rut_pasajero,None)
        self.__pasajero.quitarPasajero(pasajero)
    
    def verPasajero(self):
        return self.__pasajero.verPasajero(self)
    
    def modificarPasajero(self,rut,nombre):
        rut_pasajero = rut
        nombre_pasajero = nombre
        pasajero = Pasajero(rut_pasajero,nombre_pasajero)
        self.__pasajero.modificarPasajero(pasajero)