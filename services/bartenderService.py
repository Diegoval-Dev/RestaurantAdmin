#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection

def getDrinksBartender():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT cb.bebidaid, b.name, cb.cantidad, cb.fecha
                FROM cuenta_bebida cb
                JOIN bebida b ON cb.bebidaid = b.bebidaid
                ORDER BY cb.fecha ASC;
            """)
            drinks = cursor.fetchall()
            return {"success": True, "data": drinks}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()