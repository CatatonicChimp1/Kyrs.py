from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

# Импортируем ранее созданные модули
from library import process_data, IndexStorage, search

# Инициализация приложения и хранилища индексов
app = FastAPI()
index_storage = IndexStorage()

# Модель для входных данных
class IndexRequest(BaseModel):
    index_name: str
    data: List[Dict]

class SearchRequest(BaseModel):
    query: str
    index_name: str
    filters: Optional[Dict] = None

@app.post("/create_index/")
def create_index(request: IndexRequest):
    """
    Создает индекс из предоставленных данных.
    """
    try:
        index_storage.create_index(request.data, request.index_name)
        return {"message": f"Индекс '{request.index_name}' успешно создан."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/search/")
def search_index(request: SearchRequest):
    """
    Выполняет поиск по заданному индексу.
    """
    try:
        results = search(request.query, request.index_name, request.filters)
        return {"results": results}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/")
def read_root():
    """
    Тестовый маршрут.
    """
    return {"message": "API для библиотеки полнотекстового поиска готово к работе!"}
