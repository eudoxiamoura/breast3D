from fastapi import FastAPI

# Inicializa a aplicação
app = FastAPI()

# Rota de exemplo
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
def create_item(item: dict):
    return {"item_created": item}
