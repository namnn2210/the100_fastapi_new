from abc import ABC, abstractmethod
from typing import List, Optional
from database.database import get_db


class Repository(ABC):

    def __init__(self):
        self.db = get_db()

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def find(self, id: int):
        pass

    @abstractmethod
    def find_all(self) -> List:
        pass

    @abstractmethod
    def update(self, id: int, **kwargs):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
