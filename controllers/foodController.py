import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.foodService import serviceViewFoodMenu, serviceViewDrinkMenu, addProductToBill

"""
Esta funcion devuelve el menu de comida de la base de datos
"""
def viewFoodMenuController():
    try:
        result = serviceViewFoodMenu()
        if result["success"]:
            return result["data"]
        else:
            return []
    except Exception as e:
        return []

"""
Esta funcion devuelve el menu de bebidas de la base de datos
"""
def viewDrinkMenuController():
    try:
        result = serviceViewDrinkMenu()
        if result["success"]:
            return result["data"]
        else:
            return []
    except Exception as e:
        return []


"""
Esta funcion recine el id de un producto y la cantidad y lo agrega a la cuenta de la mesa
recibe: id del producto, cantidad, id de la cuenta
Devuelve:   {"success": True} si el producto se agrego correctamente
            {"success": False, "error": "mensaje de error"} si hubo un error en la consulta 
"""
def addProductToBillController(id, quantity, count_id):
    try:
        result = addProductToBill(id, quantity, count_id)
        if result["success"]:
            return {"success": True, "data": result}
        else:
            return []
    except Exception as e:
        return []