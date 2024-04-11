#importaciones de librerias del controller
import bcrypt
#importaciones para la ruta
import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))
#imports of modules from the project

from services.loginService import serviceRegister, getPassword, getRole


def registerController(username, password, rol):
    passwordEncripted = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        result = serviceRegister(username, passwordEncripted, rol)
        if result["success"]:
            return {"success": True, "message": "Usuario registrado exitosamente."}
        else:
            return {"success": False, "error": "Error al registar el usuario. " + result["error"]}
    except Exception as e:
        return {"success": False, "error": "Error al procesar la solicitud de registro." + str(e)}

def loginController(username, password):
    result = getPassword(username)
    encryptedPassword = result["data"]

    if result["success"] == False:
        return {"success": False, "error": encryptedPassword["error"]}
    else:
        try:
            hashed_password = encryptedPassword[0][2:]
            hashed_password = bytes.fromhex(hashed_password) 

            

            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                rol = getRole(username)
                return {"success": True, "message": "Inicio de sesión exitoso", "rol": rol[0]}
            else:
                return {"success": False, "error": "Contraseña incorrecta"}
        except Exception as e:
            return {"success": False, "error": "Error al procesar la solicitud de inicio de sesión." + str(e)}




