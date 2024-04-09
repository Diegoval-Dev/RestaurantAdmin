import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection



def serviceLogin(username, password):
    conn = get_connection()
    
def serviceRegister(username, password, rol):
    conn = get_connection()
    if conn is None:
        return {"success": False, "message": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña, rol) VALUES (%s, %s, %s)", (username, password, rol))
            conn.commit()
            return {"success": True, "message": "Usuario registrado exitosamente."}
    except Exception as e:
        return {"success": False, "message": f"Error al registrar usuario: {e}"}
    finally:
        conn.close()


def getPassword(username):
    conn = get_connection()
    if conn is None:
        return None 
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT contraseña FROM usuarios WHERE nombre_usuario = %s", (username,))
            result = cursor.fetchone()
            return result if result else None
    except Exception as e:
        return None
    finally:
        conn.close()
