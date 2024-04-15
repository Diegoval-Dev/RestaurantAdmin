#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.chefService import getPlatesChef

def viewPlatesOrdenController():
    plates = getPlatesChef()
    return plates
