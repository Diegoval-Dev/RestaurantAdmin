import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection

"""
Esta funcion devuelve el menu de comida de la base de datos
"""
def serviceViewFoodMenu():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("Aqui adentro va el Query recuerden que los parametros van con %s, para eviatar SQL injection", ("aqui van los parametros"))
            result = cursor.fetchall()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

"""
Esta funcion devuelve el menu de bebidas de la base de datos
"""
def serviceViewDrinkMenu():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("Aqui adentro va el Query recuerden que los parametros van con %s, para eviatar SQL injection", ("aqui van los parametros"))
            result = cursor.fetchall()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()