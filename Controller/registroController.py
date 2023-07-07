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

    def verRegistro(self):
        return self.__registro.verRegistro()
    
    def verRegistroId(self,id):
        registro_id = id
        return self.__registro.verTipoHabitacionId(registro_id)

    def agregarRegistro(self,habitacion,pasajero,diasHospedaje,numeroPersonas,costoAdicionalPorPersona,costoHabitacion):
        numero_habitacion = habitacion.getNumeroHabitacion()
        rut_pasajero_responsable =pasajero.getRut()
        fecha_asignacion = datetime.now()
        dias_hospedaje = diasHospedaje
        fecha_fin = datetime.now() + timedelta(days=dias_hospedaje)
        numero_personas = numeroPersonas
        costo_adicional = costoAdicionalPorPersona
        costo_habitacion = costoHabitacion
        costo_total = costo_adicional*numero_personas + costo_habitacion
        registro = Registro(None,numero_habitacion,rut_pasajero_responsable,fecha_asignacion,fecha_fin,numero_personas,costo_adicional,costo_total)
        self.__registro.agregarRegistro(registro)
        
    
    def modificarRegistro(self,idRegistro,habitacion,pasajero,nuevaFechaFin,numeroPersonas,costoAdicionalPorPersona,costoTotal):
        registro_id = idRegistro
        registro = self.__registro.verRegistroId(registro_id)
        fecha_fin = nuevaFechaFin
        habitacion_id = habitacion.getNumeroHabitacion()
        rut_responsable = pasajero.getRut()
        numero_personas = numeroPersonas
        costo_adicional = costoAdicionalPorPersona
        costo_total = costoTotal
        registro.setNumeroHabitacion(habitacion_id)
        registro.setRutPasajeroResponsable(rut_responsable)
        registro.setFechaFin(fecha_fin)
        registro.setNumeroPersonas(numero_personas)
        registro.setCostoAdicionalPorPersona(costo_adicional)
        registro.setCostoTotal(costo_total)
        self.__registro.modificarRegistro(registro)

    def elimiarRegistro(self,id):
        registro_id = id
        registro = self.__registro.verRegistroId(registro_id)
        self.__registro.quitarRegistro(registro)