import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.countService import serviceCreateNewCount, serviceViewCount, serviceGetCountID


def createCountController(tableid):
    try:
        result = serviceCreateNewCount(tableid)
        if result["success"]:
            return {"success": True, "message": "Cuenta abierta exitosamente."}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}
    

def viewCountController(countid):
    try:
        result = serviceViewCount(countid)
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}

"""
esta funcion recibe el id de una mesa y devuelve el id de la cuenta que esta abierta en esa mesa
"""
def getCountID(tableid):
    result = serviceGetCountID(tableid)
    if result["success"]:
        return result["data"][0]
    else:
        return None