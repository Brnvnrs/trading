from fastapi import FastAPI

'''
to use this API we need copy and paste this comand in terminal where this archive is  
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
and then the terminal give us a link and we can check the api

'''

app = FastAPI()
@app.get("/")

def read_root():
    usr: str = "brian"
    saludo :str = "hola " 
    res:dict = {saludo:usr}
    return res

@app.get("/users")
def user():
    return {"users":["brian", "ivan"]}

@app.get("/database")
def ddbb():
    pass