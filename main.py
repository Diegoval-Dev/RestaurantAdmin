import getpass
import os
import msvcrt
from datetime import datetime

from controllers.loginController import registerController, loginController, getId
from controllers.areaController import createAreaController, viewAreasController
from controllers.tableController import createTableController, viewTablesController, tableHasOpenBill
from controllers.waiterController import createNewWaiter
from controllers.foodController import viewFoodMenuController, addProductToBillController
from controllers.CountController import createCountController, viewCountController, getCountID
from controllers.reportsController import ServiceFoodMoreOrdersController, ServiceAverageOrderTimeController, ServiceAverageMealTimeController
from controllers.fectutaController import ClienteController
from controllers.chefController import viewPlatesOrdenController
from controllers.bartenderController import viewDrinksOrdenController

logeado = False

def viewDrinksOrden():
    clear()
    print("Bebidas ordenadas")
    result = viewDrinksOrdenController()
    if result['success']:
        print("ID\tNombre\tCantidad\tFecha")
        for drink in result['data']:
            formatted_date = datetime.strptime(drink[3], "%Y-%m-%d").strftime("%d %b %Y")
            print(f"{drink[0]}\t{drink[1]}\t{drink[2]}\t{formatted_date}")
    else:
        print("Error:", result['error'])
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

def viewPlatesOrden():
    clear()
    print("Platos ordenados")
    result = viewPlatesOrdenController()
    if result['success']:
        print("ID\tNombre\tCantidad\tFecha")
        for plate in result['data']:
            formatted_date = datetime.strptime(plate[3], "%Y-%m-%d").strftime("%d %b %Y")
            print(f"{plate[0]}\t{plate[1]}\t{plate[2]}\t{formatted_date}")
    else:
        print("Error:", result['error'])
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

def addFoodMenu(count_id):
    clear()
    print("Menú de comida")
    print("ID\tNombre\tPrecio")
    food = viewFoodMenuController()
    for f in food:
        print(f"{f[0]}\t{f[1]}\t{f[2]}")
    print("elija el id del producto para agregar a la cuenta, 0 para salir")
    id = input("Ingrese el id del producto: ")
    if id == "0":
        return
    print("Cantidad: ")
    quantity = input("Ingrese la cantidad: ")
    result = addProductToBillController(id, quantity, count_id)
    print(result)
    if result["success"]:
        print("Producto agregado con éxito. Presione cualquier tecla para continuar")
        msvcrt.getch()
    else:
        print(result["error"], " Presione cualquier tecla para continuar")
        msvcrt.getch()

def addProductToBill(count_id):
    clear()
    print("Agregar producto a la cuenta de la mesa. Cuenta: ", count_id)
    print("1. Comida")
    print("2. Bebida")
    print("3. Salir")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        addFoodMenu(count_id)
    if opcion == "2":
        pass
    if opcion == "3":
        pass

def viewBill(countid):
    clear()
    print("Cuenta de la mesa", countid)
    print("ID\tNombre\tCantidad\tPrecio\tTotal")
    result = viewCountController(countid)
    for i in result['data']:
        print(str(i[0]) + " " +  str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]))
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

def tableBill(table_id):
    isOpenBill = tableHasOpenBill(table_id)
    clear()
    if isOpenBill:
        print("La mesa tiene una cuenta abierta")
        count_id = getCountID(table_id)
        print("Que desea hacer?")
        print("1. Ver cuenta")
        print("2. Agregar a la cuenta")
        print("3. Cerrar cuenta")
        print("4. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            viewBill(count_id)
        if opcion == "2":
            addProductToBill(count_id)
        if opcion == "3":
            pass
        if opcion == "4":
            pass
    else:
        print("La mesa no tiene una cuenta abierta")
        print("Desea abrir una cuenta en la mesa?")
        print("1. Si")
        print("2. No")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            result = createCountController(table_id)
            if result["success"]:
                print("Cuenta abierta con éxito. Presione cualquier tecla para continuar")
                msvcrt.getch()
        if opcion == "2":
            pass



def bill_Print(count_id):
    clear()
    print("Factura")

    direccion = input("Ingrese la dirección del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")

    # Imprimir los detalles del cliente
    print("Detalles del Cliente:")
    print(f"Dirección: {direccion}")
    print(f"Nombre: {nombre}")
    print(f"NIT: {nit}")
    print()

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()




    
    
def selectTable():
    clear()
    print("Seleccione una mesa")
    viewTables()
    table_id = input("Ingrese el id de la mesa: ")
    print("Que desea hacer?")
    print("1. Abrir cuenta en mesa")
    print("2. Juntar mesa")
    print("3. Imprimir factura")
    print("4. Salir")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        tableBill(table_id)
    if opcion == "2":
        pass
    if opcion == "3":
       count_id = input("Ingrese el ID de la cuenta para imprimir la factura: ")
    bill_Print(count_id)
    if opcion == "4":
        pass
    else:
        print("Opción no válida")

def createUsers():
    clear()
    print("Crear nuevo usuario")
    username = input("Ingrese el nombre de usuario: ")
    password = getpass.getpass("Ingrese la contraseña: ")
    rol = input("Ingrese el rol: ")
    result = registerController(username, password, rol)
    if result["success"]:
        print("Usuario creado con éxito. Presione cualquier tecla para continuar")
        msvcrt.getch()
        id = getId(username)
        if rol == "mesero":
            print("Crear nuevo mesero")
            print("Vizualice las areas para asignar al mesero")
            viewAreas()
            areaid = input("Ingrese el id del área: ")
            name = input("Ingrese el nombre del mesero: ")
            result = createNewWaiter(areaid, name, id)
            if result["success"]:
                print("Mesero creado con éxito. Presione cualquier tecla para continuar")
                msvcrt.getch()
            else:
                print(result["error"], " Presione cualquier tecla para continuar")
                msvcrt.getch()
        if rol == "chef":
            pass
        if rol == "bartender":
            pass
        if rol == "admin":
            pass
    else:
        print(result["error"], " Presione cualquier tecla para continuar")
        msvcrt.getch()

def viewTables():
    clear()
    print("Mesas registradas")
    print("ID\tÁrea\tCapacidad\tMesa movible")
    
    result = viewTablesController() 
    tables = result["data"]

    for table in tables:
        moveable = "Sí" if table[3] else "No"
        print(f"{table[0]}\t{table[1]}\t{table[2]}\t\t{moveable}")

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()  

def createNewTable():
    clear()
    print("Crear nueva mesa")
    print/("Vizualice las áreas para asignar la mesa")
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



def takeOrder(table_id):
    addProductToBill(table_id) 

def viewOrders(table_id):
    count_id = getCountID(table_id)  
    if count_id: 
        viewBill(count_id)  
    else:
        print("No se encontró una cuenta asociada con el ID de la mesa proporcionado.")




def ServiceFoodMoreOrders():
    clear()
    print("Platos más pedidos")
    fecha_ini = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha final (YYYY-MM-DD): ")

    result = ServiceFoodMoreOrdersController(fecha_ini, fecha_fin)

    if result["success"]:
        print("Fecha\t\tCantidad de pedidos")
        for row in result["data"]:
            print(f"{row[0]}\t{row[1]}")
    else:
        print("Error:", result["error"])

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()


def ServiceAverageOrderTime():
    clear()
    print("Horario con más ingresos")
    fecha_ini = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha final (YYYY-MM-DD): ")

    result = ServiceAverageOrderTimeController(fecha_ini, fecha_fin)

    if result["success"]:
        print("Plato ID\tNombre del Plato\tTotal de Pedidos")
        for row in result["data"]:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
    else:
        print("Error:", result["error"])

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()




def ServiceAverageMealTime():
    clear()
    print("Horario con más ingresos")
    fecha_ini = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha final (YYYY-MM-DD): ")

    result = ServiceAverageMealTimeController(fecha_ini, fecha_fin)

    if result["success"]:
        print("Promedio de Comer")
        print("Personas \t Tiempo Promedio")
        for row in result["data"]:
            print(f"{row[0]} \t\t {row[1]}")
    else:
        print("Error:", result["error"])

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()




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
            print("5. Crear usuarios")
            print("6. Platos más pedidos")
            print("7. Horario con más pedidos")
            print("8. Duración de comida")
            print("12. Salir")
            opcion = input("Ingrese la opción deseada: ")

            if opcion == "1":
                createNewArea()
            if opcion == "2":
                viewAreas()
            if opcion == "3":
                createNewTable()
            if opcion == "4":
                viewTables()
            if opcion == "5":
                createUsers()
            if opcion == "6":
                ServiceFoodMoreOrders()
            if opcion == "7":
                ServiceAverageOrderTime()
            if opcion == "8":
                ServiceAverageMealTime()
            if opcion == "12":
                logeado = False
                start()
            else:
                print("Opción no válida")
        if rol == "mesero":
            print("1. Seleccionar mesa")
            print("2. Tomar pedido")
            print("3. Ver pedidos")
            print("4. Salir")
            opcion = input("Ingrese la opción deseada: ")
            if opcion == "1":
                viewTables()
                selectTable()
            if opcion == "2":
                table_id = input("Ingrese el ID de la mesa para tomar el pedido: ")
                takeOrder(table_id)
            if opcion == "3":
                table_id = input("Ingrese el ID de la mesa para ver los pedidos: ")
                viewOrders(table_id)
            if opcion == "4":
                logeado = False
                start()
            else:
                print("Opción no válida")
        if rol == "chef":
            viewPlatesOrden()
        if rol == "bartender":
            viewDrinksOrden()
        else:
            print("Opción no válida")

start()

