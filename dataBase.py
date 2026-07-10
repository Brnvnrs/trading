import psycopg2
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

