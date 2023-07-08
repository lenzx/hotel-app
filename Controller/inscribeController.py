import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Model.inscribe import Inscribe

class InscribeController:
    def __init__(self):
        self.__inscribe = Inscribe(None,None)
    
    def verInscribe(self):
        return self.__inscribe.verInscribe()
    
    def verInscribeId(self,registroId,personaRut):
        registro_id = registroId
        persona_rut = personaRut
        return self.__inscribe.verInscribeId(registro_id,persona_rut)
    
    def agregarIscribe(self,registroId,personaRut):
        registro_id = registroId
        persona_rut = personaRut
        inscribe = Inscribe(registro_id,persona_rut)
        self.__inscribe.agregarInscribe(inscribe)

    def eliminarInscribe(self,registroId,personaRut):
        registro_id = registroId
        persona_rut = personaRut
        inscribe = self.__inscribe.verInscribeId(registro_id,persona_rut)
        self.__inscribe.quitarInscribe(inscribe)