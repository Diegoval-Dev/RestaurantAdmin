import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.bartenderService import getDrinksBartender

def viewDrinksOrdenController():
    drinks = getDrinksBartender()
    return drinks