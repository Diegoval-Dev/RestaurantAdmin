import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from db.connection import get_connection
#se conecta con la base de datos

def ServiceFoodMoreOrders(fecha_ini, fecha_fin):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute(" SELECT fecha, COUNT(*) AS cantidad_pedidos FROM ( SELECT fecha FROM cuenta_bebidas WHERE fecha BETWEEN %s AND %s UNION ALL SELECT fecha FROM cuenta_plato WHERE fecha BETWEEN %s AND %s ) AS Pedidos GROUP BY fecha ORDER BY  cantidad_pedidos DESC" , (fecha_ini, fecha_fin, fecha_ini, fecha_fin))
            result = cursor.fetchall()
            return {"success": True, "message": "Reporte de platos más pedidos exitosamente", "data" : result}
    except Exception as e:
        return {"success": False, "error": "Error al obtener los datos de los platos más pedidos:" + str(e)}
    finally:
        conn.close()
        


def ServiceAverageOrderTime(fecha_ini, fecha_fin):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT p.platoid, p.name AS nombre_plato, SUM(cp.cantidad) AS total_pedidos FROM cuenta_plato cp JOIN plato p ON cp.platoid = p.platoid WHERE cp.fecha >= %s and cp.fecha <= %s GROUP BY p.platoid, p.name ORDER BY total_pedidos DESC", (fecha_ini, fecha_fin))
            result = cursor.fetchall()
            return {"success": True, "message": "Horario en el que se ingresan más pedidos", "data": result}
    except Exception as e:
        return {"success": False, "error": "Error al obtener los datos de registro de ingreso de lo más pedido: " + str(e)}
    finally:
        conn.close()


from db.connection import get_connection

def ServiceAverageMealTime(fecha_ini, fecha_fin):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT m.capacidad AS personas_comiendo, CONCAT( FLOOR(AVG(cp.duracion_comer) / 60), ' horas ', MOD(ROUND(AVG(cp.duracion_comer)), 60), ' minutos') AS promedio_tiempo_comida from cuenta_plato AS cp JOIN cuenta AS c ON cp.cuentaid = c.cuentaid JOIN mesa AS m ON c.mesaid = m.mesaid where cp.fecha BETWEEN %s AND %s GROUP BY m.capacidad", (fecha_ini, fecha_fin))
            result = cursor.fetchall()
            return {"success": True, "message": "Tiempo de comida del usuario", "data": result}
    except Exception as e:
        return {"success": False, "error": "Error al obtener los datos de tiempo en comer los clientes: " + str(e)}
    finally:
        conn.close()







def serviceComplaintByClient(date1, date2):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM queja WHERE fechahora > %s AND fechahora < %s GROUP BY clienteid, quejaid", (date1, date2))
            result = cursor.fetchall()
            return {"success": True, "message": "Quejas obtenidas con exito", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceComplaintByPlate(date1, date2):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM queja WHERE fechahora > %s AND fechahora < %s GROUP BY platoid, quejaid", (date1, date2))
            result = cursor.fetchall()
            return {"success": True, "message": "Quejas obtenidas con exito", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def serviceWaiterEfficiency():
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT meseroid, AVG(amabilidad_score) AS amabilidad, AVG(exactitud_score) AS exactitud FROM encuesta GROUP BY meseroid")
            result = cursor.fetchall()
            return {"success": True, "message": "Encuestas obtenidas obtenidas con éxito", "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()
        

