import json
from typing import List, Dict


def process_data(source: str) -> List[Dict]:
    """
    Загружает и нормализует данные из файла.

    :param source: Путь к файлу данных (JSON).
    :return: Список словарей с нормализованными данными.
    """
    try:
        with open(source, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # Пример нормализации: удаляем лишние пробелы, приводим текст к нижнему регистру
        normalized_data = [
            {key: str(value).strip().lower() for key, value in record.items()}
            for record in data
        ]
        return normalized_data
    except Exception as e:
        raise ValueError(f"Ошибка при обработке данных: {e}")


from collections import defaultdict


class IndexStorage:
    """
    Хранилище индексов для быстрого поиска.
    """

    def __init__(self):
        self.indexes = defaultdict(list)

    def create_index(self, data: List[Dict], index_name: str) -> None:
        """
        Создает индекс из нормализованных данных.

        :param data: Список нормализованных данных.
        :param index_name: Имя индекса.
        """
        if index_name in self.indexes:
            raise ValueError(f"Индекс с именем '{index_name}' уже существует.")
        for record in data:
            for key, value in record.items():
                self.indexes[index_name].append((key, value, record))
        print(f"Индекс '{index_name}' успешно создан.")


def search(query: str, index_name: str, filters: Dict = None) -> List[Dict]:
    """
    Выполняет поиск по заданному индексу.

    :param query: Поисковый запрос.
    :param index_name: Имя индекса.
    :param filters: Дополнительные фильтры для поиска.
    :return: Список найденных записей.
    """
    if index_name not in index_storage.indexes:
        raise ValueError(f"Индекс '{index_name}' не найден.")

    results = []
    for key, value, record in index_storage.indexes[index_name]:
        if query in str(value):
            if filters:
                # Проверяем, соответствует ли запись фильтрам
                if all(record.get(f_key) == f_value for f_key, f_value in filters.items()):
                    results.append(record)
            else:
                results.append(record)
    return results


# Создаем экземпляр хранилища индексов
index_storage = IndexStorage()

# Пример данных
sample_data = [
    {"id": 1, "title": "Python programming", "category": "books"},
    {"id": 2, "title": "Machine learning basics", "category": "books"},
    {"id": 3, "title": "Advanced Python", "category": "tutorials"}
]

# Шаг 1: Обработка данных
normalized_data = process_data("data/sample.json")  # Пример пути к данным

# Шаг 2: Создание индекса
index_storage.create_index(normalized_data, "sample_index")

# Шаг 3: Поиск
results = search("python", "sample_index", {"category": "books"})
print("Результаты поиска:", results)
