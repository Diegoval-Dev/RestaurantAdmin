#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection

def serviceCreateNewTable(area_id, capacity, moveable):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO mesa (areaid, capacidad, moveable) VALUES (%s, %s, %s)", (area_id, capacity, moveable))
            conn.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceViewTables():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM mesa")
            result = cursor.fetchall()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceViewTables():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM mesa")
            result = cursor.fetchall()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceGetTableArea(mesaid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT areaid FROM mesa WHERE mesaid = %s", [mesaid])
            queryResult = cursor.fetchall()
            result = queryResult[0]
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

"""
Esta funcion recine el id de una mesa y retorna si tiene una cuenta abierta o no
recibe: id de la mesa
Devuelve:   {"success": True, "data": True} si la mesa tiene una cuenta abierta
            {"success": True, "data": False} si la mesa no tiene una cuenta abierta
            {"success": False, "error": "mensaje de error"} si hubo un error en la consulta 
"""
def serviceBillOpen(tableid):
    conn = get_connection()
    if conn is None:
        print("error de conexion")
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT is_open FROM cuenta WHERE mesaid = %s", [tableid])
            queryResult = cursor.fetchone()
            result = queryResult[0]
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceViewTablesToJoin(areaid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from mesa where areaid = %s and moveable = 'true'", [areaid])
            result = cursor.fetchall()
            return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()