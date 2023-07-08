import sys
import os
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Controller.costoHabitacionController import CostoHabitacionController
from Controller.habitacionController import HabitacionController
from Controller.inscribeController import Inscribe
from Controller.pasajeroController import PasajeroController
from Controller.registroController import RegistroController
from Controller.tipoHabitacionController import TipoHabitacionController

class Coordinador:
    self