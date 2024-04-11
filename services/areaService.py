#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))


from db.connection import get_connection

def serviceCreateNewArea(name, smoker):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO area (name, smoker) VALUES (%s, %s)", (name, smoker))
            conn.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceViewAreas():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM area")
            result = cursor.fetchall()
            return {"success": True, "message": "Areas obtenidas exitosamente.", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()