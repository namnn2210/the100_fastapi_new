from repository.repository import Repository
from model.models import Category

from typing import List, Optional


class CategoryRepository(Repository):

    def create(self, **kwargs) -> Category:
        category = Category(**kwargs)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def find(self, id: int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == id).first()

    def find_all(self) -> List[Category]:
        return self.db.query(Category).all()

    def update(self, id: int, **kwargs) -> Optional[Category]:
        category = self.find(id)
        if category:
            for key, value in kwargs.items():
                setattr(category, key, value)
            self.db.commit()
            self.db.refresh(category)
        return category

    def delete(self, id: int) -> bool:
        category = self.find(id)
        if category:
            self.db.delete(category)
            self.db.commit()
            return True
        return False
