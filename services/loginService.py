#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))


from db.connection import get_connection



    
def serviceRegister(username, password, rol):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña, rol) VALUES (%s, %s, %s)", (username, password, rol))
            conn.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": e}
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
            if result:
                return {"success": True, "data": result}
            else:
                return {"success": False, "error": "Usuario no encontrado"}
    except Exception as e:
        return {"success": False, "error": "Error al obtener contraseña" + str(e)}
    finally:
        conn.close()

def getRole(username):
    conn = get_connection()
    if conn is None:
        return None 
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT rol FROM usuarios WHERE nombre_usuario = %s", (username,))
            result = cursor.fetchone()
            return result if result else None
    except Exception as e:
        return None
    finally:
        conn.close()

def getUserId(username):
    conn = get_connection()
    if conn is None:
        return None 
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre_usuario = %s", (username,))
            result = cursor.fetchone()
            return result if result else None
    except Exception as e:
        return None
    finally:
        conn.close()
