#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection

"""
Esta funcion recine el id de una mesa y le abre una cuenta en la base de datos
recibe: id de la mesa
Devuelve:   {"success": True} si la cuenta se abrio correctamente
            {"success": False, "error": "mensaje de error"} si hubo un error en la consulta 
"""
def serviceCreateNewCount(tableid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("insert into cuenta(mesaid, is_open) values (%s, true)", [tableid])
            conn.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceCloseCount(countid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("update cuenta set is_open = false where countid = %s", [countid])
            conn.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

"""
Esta funcion devuelve una cuenta de la base de datos
"""
def serviceViewCount(countid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cp.platoid AS ID, p.name AS Nombre, cp.cantidad AS Cantidad, p.price AS Precio, cp.cantidad * p.price AS Total FROM cuenta_plato cp JOIN plato p ON cp.platoid = p.platoid WHERE cp.cuentaid = %s", [countid])
            result = cursor.fetchall()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()


"""
esta funcion recibe el id de una mesa y devuelve el id de la cuenta que esta abierta en esa mesa
"""
def serviceGetCountID(tableid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cuentaid FROM cuenta WHERE mesaid = %s", [tableid])
            result = cursor.fetchone()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()
