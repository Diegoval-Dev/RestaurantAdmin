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
            cursor.execute("SELECT p.platoid, p.name AS nombre_plato, SUM(cp.cantidad) AS total_pedidos FROM cuenta_plato cp JOIN plato p ON cp.platoid = p.platoid WHERE cp.fecha >= %s and cp.fecha <= %s GROUP BY p.platoid, p.name ORDER BY total_pedidos DESC", (fecha_ini, fecha_fin, fecha_ini, fecha_fin))
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
            cursor.execute("", (fecha_ini, fecha_fin, fecha_ini, fecha_fin))
            result = cursor.fetchall()
            return {"success": True, "message": "Horario en el que se ingresan más pedidos", "data": result}
    except Exception as e:
        return {"success": False, "error": "Error al obtener los datos de registro de ingreso de lo más pedido: " + str(e)}
    finally:
        conn.close()



def ServiceAverageMealTime(fecha_ini, fecha_fin):
    conn = get_connection()
    if conn is None:
        return {"success": False, "error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT CONCAT(personas_comiendo, ' personas: ', FLOOR(promedio_tiempo_comida / 60), ' horas ', promedio_tiempo_comida % 60, ' minutos') AS resultado FROM (SELECT ROUND(AVG(duracion_comer)) AS promedio_tiempo_comida, m.capacidad AS personas_comiendo FROM cuenta_plato AS cp JOIN cuenta AS c ON cp.cuentaid = c.cuentaid JOIN mesa AS m ON c.mesaid = m.mesaid JOIN ( SELECT c.mesaid, COUNT(*) AS num_registros, SUM(cp.duracion_comer) AS suma_tiempo_comida FROM cuenta_plato AS cp JOIN cuenta AS c ON cp.cuentaid = c.cuentaid WHERE cp.fecha BETWEEN '2024-03-01' AND '2024-04-10'GROUP BY c.mesaid ) AS tiempos ON c.mesaid = tiempos.mesaid GROUP BY m.capacidad ) AS subconsulta;", (fecha_ini, fecha_fin, fecha_ini, fecha_fin))
            result = cursor.fetchall()
            return {"success": True, "message": "Tiempo de comida del usuario",  "data": result}
    except Exception as e:
        return {"success": False, "error": "Error al obtener los datos de tiempo en comer los clientes: " + str(e)}
    finally:
        conn.close()
        

