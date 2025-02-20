from typing import List, Dict
import json


class IndexStorage:
    """
    Класс для хранения и управления индексами.
    """

    def __init__(self):
        self.indices = {}

    def create_index(self, data: List[Dict], index_name: str):
        """
        Создает индекс с указанным именем и данными.
        """
        if index_name in self.indices:
            raise ValueError(f"Индекс '{index_name}' уже существует.")
        processed_data = process_data(data)
        self.indices[index_name] = processed_data

    def get_index(self, index_name: str) -> List[Dict]:
        """
        Возвращает данные индекса по имени.
        """
        if index_name not in self.indices:
            raise ValueError(f"Индекс '{index_name}' не найден.")
        return self.indices[index_name]


def process_data(data: List[Dict]) -> List[Dict]:
    """
    Обрабатывает данные перед индексацией.
    """
    processed_data = []
    for item in data:
        if "text" in item:
            processed_text = item["text"].strip().lower()
            processed_data.append({"id": item["id"], "text": processed_text})
    return processed_data


def search(query: str, index_name: str, index_storage: IndexStorage, filters: Dict = None) -> List[Dict]:
    """
    Выполняет поиск по индексу.
    """
    index = index_storage.get_index(index_name)
    results = []

    for item in index:
        if query.lower() in item["text"]:
            if filters:
                match = all(item.get(key) == value for key, value in filters.items())
                if match:
                    results.append(item)
            else:
                results.append(item)
    return results
