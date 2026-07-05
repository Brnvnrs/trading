from fastapi import FastAPI

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