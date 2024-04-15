#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection

def Cliente(countid):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            # Consulta para obtener los detalles del cliente asociado con la cuenta
            cursor.execute("""
                SELECT *
                FROM cliente AS c
                JOIN cuenta AS cu ON c.clienteid = cu.cuentaid
                WHERE cu.cuentaid = %s
            """, (countid))
            cliente_data = cursor.fetchone()

            return {"success": True, "cliente_data": cliente_data}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()
        


   



