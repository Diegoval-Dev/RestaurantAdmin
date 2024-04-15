#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.tableService import *

def createTableController(area_id, capacity, moveable):
    try:
        result = serviceCreateNewTable(area_id, capacity, moveable)
        if result["success"]:
            return {"success": True, "message": "Mesa registrada exitosamente."}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}
    
def viewTablesController():
    try:
        result = serviceViewTables()
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}

def getTableAreaController(tableid):
    try:
        result = serviceGetTableArea(tableid)
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}

def viewTablesToJoinController(areaid):
    try:
        result = serviceViewTablesToJoin(areaid)
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}
    
def tableHasOpenBill(tableid):
    billOpen = serviceBillOpen(tableid)
    if billOpen["success"]:
        return True
    else:
        return False
    


