#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.areaService import serviceCreateNewArea, serviceViewAreas


def createAreaController(name, smoke):
    try:
        result = serviceCreateNewArea(name, smoke)
        if result["success"]:
            return {"success": True, "message": "Area registrada exitosamente."}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}

def viewAreasController():
    try:
        result = serviceViewAreas()
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}