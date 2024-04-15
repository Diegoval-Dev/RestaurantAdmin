#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection

def getPlatesChef():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT cp.platoid, p.name, cp.cantidad, cp.fecha
                FROM cuenta_plato cp
                JOIN plato p ON cp.platoid = p.platoid
                ORDER BY cp.fecha ASC;
            """)
            plates = cursor.fetchall()
            return {"success": True, "data": plates}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()
