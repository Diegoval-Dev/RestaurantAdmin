import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))


from db.connection import get_connection

def serviceComplaintByClient(date1, date2):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM queja WHERE fechahora > %s AND fechahora < %s GROUP BY clienteid, quejaid", (date1, date2))
            result = cursor.fetchall()
            return {"success": True, "message": "Quejas obtenidas con exito", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceComplaintByPlate(date1, date2):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM queja WHERE fechahora > %s AND fechahora < %s GROUP BY platoid, quejaid", (date1, date2))
            result = cursor.fetchall()
            return {"success": True, "message": "Quejas obtenidas con exito", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceWaiterEfficiency():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT meseroid, AVG(amabilidad_score) AS amabilidad, AVG(exactitud_score) AS exactitud FROM encuesta GROUP BY meseroid")
            result = cursor.fetchall()
            return {"success": True, "message": "Encuestas obtenidas obtenidas con éxito", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()