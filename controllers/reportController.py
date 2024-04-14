import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.reportService import serviceComplaintByClient, serviceComplaintByPlate, serviceWaiterEfficiency

def getComplaintByClientController(date1, date2):
    try:
        result = serviceComplaintByClient(date1, date2)
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error en la solicitud: " + str(e)}
    
def getComplaintByPlateController(date1, date2):
    try:
        result = serviceComplaintByPlate(date1, date2)
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error en la solicitud: " + str(e)}
    
def getWaiterEfficiencyController():
    try:
        result = serviceWaiterEfficiency()
        if result["success"]:
            return {"success": True, "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error en la solicitud: " + str(e)}
