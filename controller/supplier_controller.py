from model.models import Supplier
from model.schemas import SupplierBase
from repository.supplier_repository import SupplierRepository

supplier_repository = SupplierRepository()


def create_supplier(supplier: SupplierBase):
    supplier_repository.create(**supplier.dict())
    return supplier


def find_supplier(supplier_id: int):
    return supplier_repository.find(supplier_id)


def find_all_supplier():
    return supplier_repository.find_all()


def update_supplier(supplier_id: int, supplier: SupplierBase):
    return supplier_repository.update(supplier_id, **supplier.dict())


def delete_supplier(supplier_id: int):
    return supplier_repository.delete(supplier_id)
