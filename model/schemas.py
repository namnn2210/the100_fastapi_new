from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class SupplierBase(BaseModel):
    name: str
    address: str
    description: str
