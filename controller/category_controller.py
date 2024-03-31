from model.models import Category
from model.schemas import CategoryBase
from repository.category_repository import CategoryRepository

category_repository = CategoryRepository()


def create_category(category: CategoryBase):
    return category_repository.create(**category.dict())


def find_category(category_id: int):
    return category_repository.find(category_id)


def find_all_category():
    return category_repository.find_all()


def update_category(category_id: int, category: CategoryBase):
    return category_repository.update(category_id, **category.dict())


def delete_category(category_id: int):
    return category_repository.delete(category_id)
