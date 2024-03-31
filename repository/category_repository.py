from repository.repository import Repository
from model.models import Category

from typing import List, Optional


class CategoryRepository(Repository):

    def create(self, **kwargs) -> Category:
        category = Category(**kwargs)
        try:
            self.db.add(category)
            self.db.flush()
            self.db.refresh(category)
            print(category.__dict__)
            return category
        except Exception as e:
            self.db.rollback()
            print("An error occurred while creating the category:", str(e))
            return category

    def find(self, id: int) -> Optional[Category]:
        try:
            return self.db.query(Category).filter(Category.id == id).first()
        except Exception as e:
            print("An error occurred while finding the category:", str(e))
            return None

    def find_all(self) -> List[Category]:
        try:
            return self.db.query(Category).all()
        except Exception as e:
            print("An error occurred while finding all categories:", str(e))
            return []

    def update(self, id: int, **kwargs) -> Optional[Category]:
        category = self.find(id)
        if category:
            try:
                for key, value in kwargs.items():
                    setattr(category, key, value)
                self.db.flush()
                self.db.refresh(category)
                return category
            except Exception as e:
                self.db.rollback()
                print("An error occurred while updating the category:", str(e))
                return None
        return None

    def delete(self, id: int) -> bool:
        category = self.find(id)
        if category:
            try:
                self.db.delete(category)
                self.db.flush()
                return True
            except Exception as e:
                self.db.rollback()
                print("An error occurred while deleting the category:", str(e))
                return False
        return False
