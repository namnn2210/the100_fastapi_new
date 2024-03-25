from repository.repository import Repository
from model.models import Supplier

from typing import List, Optional


class SupplierRepository(Repository):

    def create(self, **kwargs) -> Supplier:
        supplier = Supplier(**kwargs)
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        return supplier

    def find(self, id: int) -> Optional[Supplier]:
        return self.db.query(Supplier).filter(Supplier.id == id).first()

    def find_all(self) -> List[Supplier]:
        return self.db.query(Supplier).all()

    def update(self, id: int, **kwargs) -> Optional[Supplier]:
        supplier = self.find(id)
        if supplier:
            for key, value in kwargs.items():
                setattr(supplier, key, value)
            self.db.commit()
            self.db.refresh(supplier)
        return supplier

    def delete(self, id: int) -> bool:
        supplier = self.find(id)
        if supplier:
            self.db.delete(supplier)
            self.db.commit()
            return True
        return False
