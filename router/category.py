from fastapi import APIRouter, Depends, HTTPException
from model.schemas import CategoryBase
from controller import category_controller

router = APIRouter()


@router.post("/category", tags=["Category"])
async def create_category(category: CategoryBase):
    category = category_controller.create_category(category)
    return category


@router.get("/category/{category_id}", tags=["Category"])
async def find_category(category_id: int):
    return category_controller.find_category(category_id)


@router.get("/category", tags=["Category"])
async def find_all_category():
    return category_controller.find_all_category()


@router.put("/category", tags=["Category"])
async def update_category(category_id: int, category: CategoryBase):
    return category_controller.update_category(category_id, category)


@router.delete("/category", tags=["Category"])
async def delete_category(category_id: int):
    return category_controller.delete_category(category_id)
