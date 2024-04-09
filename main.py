import getpass

from controllers.loginController import registerController, loginController
from controllers.waiterController import createNewWaiter



logeado = False

def login():
    global logeado
    username = input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    result = loginController(username, password)
    
    if result["success"]:
        print("Inicio de sesión exitoso")
        rol = result["rol"]
        logeado = True
        dashboard(rol)
    else:
        print("Error al iniciar sesión:", result["message"])
        start()
    

def signin():
    global logeado
    
    print("Registrarse")
    username = input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ") 
    rol = input("Ingrese su rol: ")
    
    result = registerController(username, password, rol)  
    
    if result["success"]: 
        print("Usuario registrado con éxito")
        logeado = True
        dashboard(rol)
        
        if rol == "mesero":
            areaid = input("Ingrese el ID area: ")
            name = input("Ingrese su nombre: ")
            createNewWaiter(areaid, name)
        
    else:
        print("Error al registrar usuario:", result["message"])
        start()


def start():
    print("Bienvenido al sistema")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    inicio = input("Ingrese la opción deseada: ")
    if inicio == "1":
        login()
    elif inicio == "2":
        signin()
    elif inicio == "3":
        exit()
    else:
        print("Opción no válida")


def dashboard(rol):
    print("Bienvenido al dashboard", rol)

start()

