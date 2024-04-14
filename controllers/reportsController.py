import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.reportsService import ServiceFoodMoreOrders, ServiceAverageOrderTime, ServiceAverageMealTime


def ServiceFoodMoreOrdersController(fecha_ini, fecha_fin):
    try:
        result = ServiceFoodMoreOrders(fecha_ini, fecha_fin)
        if result["success"]:
            return {"success": True, "message": "Reporte de platos más pedidos exitosamente."}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al ejecutar la consulta: " + str(e)}


def ServiceAverageOrderTimeController(fecha_ini, fecha_fin):
    try:
        result = ServiceAverageOrderTime(fecha_ini, fecha_fin)
        if result["success"]:
            return {"success": True, "message": "Horario en el que se ingresan más pedidos exitosamente."}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al ejecutar la consulta: " + str(e)}

def ServiceAverageMealTimeController(parametros):
    try:
        result = ServiceAverageMealTime(parametros)
        if result["success"]:
            return {"success": True, "message": "Tiempo de comida del usuario"}
        else:
            return {"success": False, "error": result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al ejecutar la consulta: " + str(e)}







