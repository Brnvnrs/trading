import psycopg2

conn = psycopg2.connect(
    dbname = "trading_bot",
    user = "postgres",
    password = "postgres",
    host="localhost",
    port="5432"
) 
cur = conn.cursor()

cur.execute(
    "SELECT * FROM operaciones"
    )
#to insert data we can use
#cur.execute("INSERT INTO operaciones (moneda, monto, precio, tipo) VALUES (%s,%s,%s,%s)",("ETHUSDT",0.004, 2450.0, True) # T compra, F venta) 
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()



# aca habria que crear una base de datos, y guardar 
# moneda, monto, precio de la moneda, venta/compra,dia y hora

# despues habria que crear la api y que devuelva todas lascompras y las ventas que se hicieron 
# basicamente un historial.

import os
from pathlib import Path
from dotenv import load_dotenv

class DataBase:
    #atributos
    db_name:str
    db_user:str
    db_password:str
    db_host:str
    db_port:str
    path:str

    #constructor
    def __init__(self):
        self.path="/home/brian/Documentos/.env.db"
        load_dotenv(dotenv_path=self.path, override=True)

        self.db_name=os.getenv("DB_NAME")
        self.db_user=os.getenv("DB_USER")
        self.db_password=os.getenv("DB_PASSWORD")
        self.db_host=os.getenv("DB_HOST")
        self.db_port=os.getenv("DB_PORT")

    #demas metodos de la clase
    def conectDDBB(self):
        '''connect to the data base'''
        res =  psycopg2.connect(**{
            "dbname" : self.db_name,
            "user" : self.db_user,
            "password": self.db_password,
            "host":self.db_host,
            "port":self.db_port
            })
        return res 
    def insertData(self, currency:str,amount:float,price:float,buyOrSell:str):
        ''' 
        going to insert an order 
        '''
        conn = self.conectDDBB()
        cur = conn.cursor()
        cur.execute("INSERT INTO operaciones (moneda, monto, precio, operacion) VALUES (%s,%s,%s,%s)",(currency,amount,price,buyOrSell))
        conn.commit()   # confirma la transacción, sin esto no se guarda nada
        cur.close()     # libera el cursor
        conn.close()    # cierra la conexión

