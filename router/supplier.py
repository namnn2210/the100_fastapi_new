from fastapi import APIRouter, Depends, HTTPException
from model.schemas import SupplierBase
from controller import supplier_controller

router = APIRouter()


@router.post("/supplier", tags=["Supplier"])
async def create_supplier(supplier: SupplierBase):
    supplier = supplier_controller.create_supplier(supplier)
    return supplier


@router.get("/supplier/{supplier_id}", tags=["Supplier"])
async def find_supplier(supplier_id: int):
    return supplier_controller.find_supplier(supplier_id)


@router.get("/supplier", tags=["Supplier"])
async def find_all_supplier():
    return supplier_controller.find_all_supplier()


@router.put("/supplier", tags=["Supplier"])
async def update_supplier(supplier_id: int, supplier: SupplierBase):
    return supplier_controller.update_supplier(supplier_id, supplier)


@router.delete("/supplier", tags=["Supplier"])
async def delete_supplier(supplier_id: int):
    return supplier_controller.delete_supplier(supplier_id)
