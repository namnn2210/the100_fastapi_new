from repository.repository import Repository
from model.models import Supplier

from typing import List, Optional


class SupplierRepository(Repository):

    def create(self, **kwargs) -> Supplier:
        supplier = Supplier(**kwargs)
        try:
            self.db.add(supplier)
            self.db.flush()
            self.db.refresh(supplier)
            return supplier
        except Exception as e:
            self.db.rollback()
            print("An error occurred while creating the supplier:", str(e))
            return supplier

    def find(self, id: int) -> Optional[Supplier]:
        try:
            return self.db.query(Supplier).filter(Supplier.id == id).first()
        except Exception as e:
            print("An error occurred while finding the supplier:", str(e))
            return None

    def find_all(self) -> List[Supplier]:
        try:
            return self.db.query(Supplier).all()
        except Exception as e:
            print("An error occurred while finding all suppliers:", str(e))
            return []

    def update(self, id: int, **kwargs) -> Optional[Supplier]:
        supplier = self.find(id)
        if supplier:
            try:
                for key, value in kwargs.items():
                    setattr(supplier, key, value)
                self.db.flush()
                self.db.refresh(supplier)
                return supplier
            except Exception as e:
                self.db.rollback()
                print("An error occurred while updating the supplier:", str(e))
                return None
        return None

    def delete(self, id: int) -> bool:
        supplier = self.find(id)
        if supplier:
            try:
                self.db.delete(supplier)
                self.db.flush()
                return True
            except Exception as e:
                self.db.rollback()
                print("An error occurred while deleting the supplier:", str(e))
                return False
        return False
