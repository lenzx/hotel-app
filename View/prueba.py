import sys
import os
from datetime import datetime,timedelta
# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta del directorio raíz al sistema de rutas de Python
sys.path.append(root_dir)
from Controller.registroController import RegistroController
from Controller.habitacionController import HabitacionController
from Controller.costoHabitacionController import 
from Controller.inscribeController import 
from Controller.tipoHabitacionController import
from Controller.pasajeroController import PasajeroController
