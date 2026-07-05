import psycopg2

conn = psycopg2.connect(
    dbname = "trading_bot",
    user = "postgres",
    password = "postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT * FROM operaciones")
#to insert data we can user 
#cur.execute("INSERT INTO operaciones (moneda, monto, precio, tipo) VALUES (%s,%s,%s,%s)",("ETHUSDT",0.004, 2450.0, True) # T compra, F venta) 
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()



# aca habria que crear una base de datos, y guardar 
# moneda, monto, precio de la moneda, venta/compra,dia y hora

# despues habria que crear la api y que devuelva todas lascompras y las ventas que se hicieron 
# basicamente un historial.



class DataBase:
    #atributos

    #constructor
    def __init__(self):
        pass

    #demas metodos de la clase
    def conectDDBB():
        pass