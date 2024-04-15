import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.reportsService import ServiceFoodMoreOrders, ServiceAverageOrderTime, ServiceAverageMealTime, serviceComplaintByClient, serviceComplaintByPlate, serviceWaiterEfficiency


def ServiceFoodMoreOrdersController(fecha_ini, fecha_fin):
    try:
        result = ServiceFoodMoreOrders(fecha_ini, fecha_fin)
        if result["success"]:
            return {"success": True, "message": "Reporte de platos más pedidos exitosamente.", "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al ejecutar la consulta: " + str(e)}

def ServiceAverageOrderTimeController(fecha_ini, fecha_fin):
    try:
        result = ServiceAverageOrderTime(fecha_ini, fecha_fin)
        if result["success"]:
            return {"success": True, "message": "Horario en el que se ingresan más pedidos exitosamente.", "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al ejecutar la consulta: " + str(e)}


def ServiceAverageMealTimeController(fecha_ini, fecha_fin):
    try:
        result = ServiceAverageMealTime(fecha_ini, fecha_fin)
        if result["success"]:
            return {"success": True, "message": "Tiempo de comida del usuario", "data": result["data"]}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al ejecutar la consulta: " + str(e)}



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

