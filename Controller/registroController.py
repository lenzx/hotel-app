import sys
import os
from datetime import datetime,timedelta
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Model.registro import Registro

class RegistroController:
    def __init__(self):
        self.__registro = Registro(None,None,None,None,None,None,None,None)

    def agregarRegistro(self,numeroHabitacion,rutPasajeroResponsable,numeroPersonas,costoAdicionalPorPersona,diasHospedaje,costoHabitacion):
        numero_habitacion = numeroHabitacion
        rut_pasajero_responsable =rutPasajeroResponsable
        numero_personas =numeroPersonas
        fecha_asignacion = datetime.now()
        dias_hospedaje = diasHospedaje
        fecha_fin = datetime.now() + timedelta(days=dias_hospedaje)
        costo_adicional = costoAdicionalPorPersona
        costo_habitacion = costoHabitacion
        costo_total = costo_adicional*numero_personas + costo_habitacion
        
    def agregarRegistro1(self,habitacion,resposable,diasHospedaje,numeroPersonas,costoAdicionalPorPersona,costoHabitacion):
        numero_habitacion = habitacion.getNumeroHabitacion()
        rut_pasajero_responsable =resposable.getRut()
        fecha_asignacion = datetime.now()
        dias_hospedaje = diasHospedaje
        fecha_fin = datetime.now() + timedelta(days=dias_hospedaje)
        numero_personas = numeroPersonas
        costo_adicional = costoAdicionalPorPersona
        costo_habitacion = costoHabitacion
        costo_total = costo_adicional*numero_personas + costo_habitacion
        registro = Registro(None,numero_habitacion,rut_pasajero_responsable,fecha_asignacion,fecha_fin,numero_personas,costo_adicional,costo_total)
        self.__registro.agregarRegistro(registro)
        
