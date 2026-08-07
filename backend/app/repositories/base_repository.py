from typing import Generic, TypeVar, Type, Optional, List, Dict, Any, Union
from sqlalchemy import select, func, delete as sql_delete
from sqlalchemy.orm import Session
from ..models.base import BaseEntity

ModelType = TypeVar("ModelType", bound=BaseEntity)


class BaseRepository(Generic[ModelType]):
    """
    Generic Base Repository implementing standard data access operations
    using SQLAlchemy 2.x unified select() queries and type-safe Generic bindings.
    """

    def __init__(self, model: Type[ModelType]) -> None:
        """
        Initializes the repository with the target model class.
        """
        self.model = model

    def create(self, db: Session, obj_in: Union[Dict[str, Any], Any]) -> ModelType:
        """
        Persists a new entity instance in the database.
        Accepts dictionary attributes or instantiated model objects.
        """
        if isinstance(obj_in, dict):
            db_obj = self.model(**obj_in)
        elif isinstance(obj_in, self.model):
            db_obj = obj_in
        else:
            obj_data = getattr(obj_in, "__dict__", {})
            clean_data = {k: v for k, v in obj_data.items() if not k.startswith("_")}
            db_obj = self.model(**clean_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """
        Retrieves a single entity by its primary key ID.
        """
        stmt = select(self.model).where(self.model.id == id)
        return db.scalar(stmt)

    def get_by_uuid(self, db: Session, uuid_str: str) -> Optional[ModelType]:
        """
        Retrieves a single entity by its unique UUID string.
        """
        stmt = select(self.model).where(self.model.uuid == uuid_str)
        return db.scalar(stmt)

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Retrieves a list of entities with pagination offsets.
        """
        stmt = select(self.model).offset(skip).limit(limit)
        return list(db.scalars(stmt).all())

    def update(self, db: Session, db_obj: ModelType, obj_in: Union[Dict[str, Any], Any]) -> ModelType:
        """
        Updates attributes of an existing entity instance.
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = getattr(obj_in, "__dict__", {})

        for field, value in update_data.items():
            if not field.startswith("_") and hasattr(db_obj, field):
                setattr(db_obj, field, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> bool:
        """
        Deletes an entity by primary key ID.
        Returns True if an entity was deleted, False otherwise.
        """
        obj = self.get(db, id)
        if not obj:
            return False
        db.delete(obj)
        db.commit()
        return True

    def exists(self, db: Session, id: int) -> bool:
        """
        Checks whether an entity with the specified primary key ID exists.
        """
        stmt = select(func.count()).select_from(self.model).where(self.model.id == id)
        count_result = db.scalar(stmt)
        return bool(count_result and count_result > 0)

    def count(self, db: Session) -> int:
        """
        Returns the total count of records in the entity table.
        """
        stmt = select(func.count()).select_from(self.model)
        count_result = db.scalar(stmt)
        return count_result or 0

    def paginate(self, db: Session, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
        """
        Returns a paginated payload containing total count, pages, items, page, and page_size.
        """
        safe_page = max(1, page)
        safe_size = max(1, min(100, page_size))
        total_items = self.count(db)
        total_pages = (total_items + safe_size - 1) // safe_size if total_items > 0 else 1
        skip = (safe_page - 1) * safe_size

        items = self.get_all(db, skip=skip, limit=safe_size)

        return {
            "items": items,
            "total": total_items,
            "page": safe_page,
            "page_size": safe_size,
            "total_pages": total_pages,
            "has_next": safe_page < total_pages,
            "has_previous": safe_page > 1
        }
