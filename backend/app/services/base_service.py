from typing import Generic, TypeVar, Optional, List, Dict, Any, Union
from sqlalchemy.orm import Session
from ..models.base import BaseEntity
from ..repositories.base_repository import BaseRepository

ModelType = TypeVar("ModelType", bound=BaseEntity)


class BaseService(Generic[ModelType]):
    """
    Generic Base Service layer encapsulating domain business logic.
    Delegates standard data access operations to an injected BaseRepository instance.
    """

    def __init__(self, repository: BaseRepository[ModelType]) -> None:
        """
        Initializes the service with an injected repository instance.
        """
        self.repository = repository

    def create(self, db: Session, obj_in: Union[Dict[str, Any], Any]) -> ModelType:
        """
        Executes creation workflow by delegating to repository.
        """
        return self.repository.create(db, obj_in)

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """
        Retrieves a single entity by primary key ID via repository.
        """
        return self.repository.get(db, id)

    def get_by_uuid(self, db: Session, uuid_str: str) -> Optional[ModelType]:
        """
        Retrieves a single entity by unique UUID via repository.
        """
        return self.repository.get_by_uuid(db, uuid_str)

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Retrieves paginated entity list via repository.
        """
        return self.repository.get_all(db, skip=skip, limit=limit)

    def update(self, db: Session, db_obj: ModelType, obj_in: Union[Dict[str, Any], Any]) -> ModelType:
        """
        Executes update workflow by delegating to repository.
        """
        return self.repository.update(db, db_obj, obj_in)

    def delete(self, db: Session, id: int) -> bool:
        """
        Executes deletion workflow by delegating to repository.
        """
        return self.repository.delete(db, id)

    def exists(self, db: Session, id: int) -> bool:
        """
        Checks entity existence via repository.
        """
        return self.repository.exists(db, id)

    def count(self, db: Session) -> int:
        """
        Returns entity count via repository.
        """
        return self.repository.count(db)

    def paginate(self, db: Session, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
        """
        Returns paginated payload via repository.
        """
        return self.repository.paginate(db, page=page, page_size=page_size)
