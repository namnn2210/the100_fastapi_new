from repository.repository import Repository
from model.models import Supplier

from typing import List, Optional


class SupplierRepository(Repository):

    def create(self, **kwargs) -> Supplier:
        supplier = Supplier(**kwargs)
        try:
            self.db.add(supplier)
            self.db.commit()
            self.db.refresh(supplier)
            return supplier
        except SQLAlchemyError as e:
            self.db.rollback()
            print("An error occurred while creating the supplier:", str(e))
            return supplier

    def find(self, id: int) -> Optional[Supplier]:
        try:
            return self.db.query(Supplier).filter(Supplier.id == id).first()
        except SQLAlchemyError as e:
            print("An error occurred while finding the supplier:", str(e))
            return None

    def find_all(self) -> List[Supplier]:
        try:
            return self.db.query(Supplier).all()
        except SQLAlchemyError as e:
            print("An error occurred while finding all suppliers:", str(e))
            return []

    def update(self, id: int, **kwargs) -> Optional[Supplier]:
        supplier = self.find(id)
        if supplier:
            try:
                for key, value in kwargs.items():
                    setattr(supplier, key, value)
                self.db.commit()
                self.db.refresh(supplier)
                return supplier
            except SQLAlchemyError as e:
                self.db.rollback()
                print("An error occurred while updating the supplier:", str(e))
                return None
        return None

    def delete(self, id: int) -> bool:
        supplier = self.find(id)
        if supplier:
            try:
                self.db.delete(supplier)
                self.db.commit()
                return True
            except SQLAlchemyError as e:
                self.db.rollback()
                print("An error occurred while deleting the supplier:", str(e))
                return False
        return False
