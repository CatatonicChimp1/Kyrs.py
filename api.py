from fastapi import FastAPI, HTTPException
from library import IndexStorage, search

app = FastAPI()
index_storage = IndexStorage()

@app.post("/create_index/")
def create_index(index_name: str, data: list):
    """
    Создает новый индекс.
    """
    try:
        index_storage.create_index(data, index_name)
        return {"message": f"Индекс '{index_name}' успешно создан."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/search/")
def search_index(query: str, index_name: str):
    """
    Выполняет поиск по индексу.
    """
    try:
        results = search(query, index_name, index_storage)
        return {"results": results}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
