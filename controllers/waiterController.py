#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.waiterService import serviceCreateNewWaiter

def createNewWaiter(areaid, name, id):
    try:
        result = serviceCreateNewWaiter(areaid, name, id)
        if result["success"]:
            return {"success": True, "message": "Mesero registrado exitosamente."}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}