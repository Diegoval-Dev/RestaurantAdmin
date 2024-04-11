import getpass
import os
import msvcrt

from controllers.loginController import registerController, loginController
from controllers.areaController import createAreaController, viewAreasController
from controllers.tableController import createTableController, viewTablesController
from controllers.waiterController import createNewWaiter

logeado = False

def viewTables():
    clear()
    print("Mesas registradas")
    print("ID\tÁrea\tCapacidad\tMesa movible")
    
    result = viewTablesController() 
    tables = result["data"]

    for table in tables:
        moveable = "Sí" if table[3] else "No"
        print(f"{table[0]}\t{table[1]}\t{table[2]}\t{moveable}")

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()  

def createNewTable():
    clear()
    print("Crear nueva mesa")
    viewAreas()
    area_id = input("Ingrese el id del área: ")
    capacity = input("Ingrese la capacidad de la mesa: ")
    moveable = input("¿Es mesa movible? (s/n): ")
    if moveable == "s":
        moveable = True
    else:
        moveable = False
    result = createTableController(area_id, capacity, moveable)
    if result["success"]:
        print("Mesa creada con éxito. Presione cualquier tecla para continuar")
        msvcrt.getch()
    else:
        print(result["error"], " Presione cualquier tecla para continuar")
        msvcrt.getch()

def viewAreas():
    clear()
    print("Áreas registradas")
    print("ID\tNombre\tFumadores")
    
    result = viewAreasController() 
    areas = result["data"]

    for area in areas:
        smoker_status = "Sí" if area[2] else "No"
        print(f"{area[0]}\t{area[1]}\t{smoker_status}")

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()  

def clear():
    os.system('cls')

def createNewArea():
    clear()
    print("Crear nueva area")
    name = input("Ingrese el nombre del area: ")
    smoke = input("¿Es área de fumadores? (s/n): ")
    if smoke == "s":
        smoke = True
    else:
        smoke = False
    result = createAreaController(name, smoke)
    if result["success"]:
        print("Area creada con éxito. Presione cualquier tecla para continuar")
        msvcrt.getch()
    else:
        print(result["error"], " Presione cualquier tecla para continuar")
        msvcrt.getch()

def login():
    clear()
    global logeado
    username = input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    result = loginController(username, password)
    if result["success"]:
        rol = result["rol"]
        logeado = True
        print("Inicio de sesión exitoso. Presione cualquier tecla para continuar")
        msvcrt.getch()
        dashboard(rol)
    else:
        print(result["error"], " Presione cualquier tecla para continuar")
        msvcrt.getch()
        start()

def signin():
    global logeado

    clear()
    
    print("Registrarse")
    username = input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ") 
    rol = input("Ingrese su rol: ")
    
    result = registerController(username, password, rol)  
    
    if result["success"]: 
        logeado = True
        print("Usuario registrado con éxito. Presione cualquier tecla para continuar")
        msvcrt.getch()
        dashboard(rol)
    else:
        print(result["error"]," Presione cualquier tecla para continuar")
        msvcrt.getch()
        start()


def start():
    clear()
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
    global logeado
    while logeado:
        clear()
        print("Bienvenido al dashboard", rol)

        if rol == "admin":
            print("1. Crear Areas")
            print("2. Ver Areas")
            print("3. Crear Mesa")
            print("4. Ver Mesas")
            print("6. Salir")
            opcion = input("Ingrese la opción deseada: ")

            if opcion == "1":
                createNewArea()
            if opcion == "2":
                viewAreas()
            if opcion == "3":
                createNewTable()
            if opcion == "4":
                viewTables()
            if opcion == "6":
                logeado = False
                start()
            else:
                pass
        else:
            print("2. Ver menú")
            print("3. Realizar pedido")
            print("4. Ver pedidos")
            print("5. Log out")
            opcion = input("Ingrese la opción deseada: ")
            if opcion == "5":
                logeado = False
                start()
            else:
                print("Opción no válida")
                dashboard(rol)

start()

