from typing import Generic, TypeVar

RepoType = TypeVar("RepoType")


class BaseService(Generic[RepoType]):
    """
    Generic service layer base class encapsulating business logic.
    Placeholder architecture for Sprint 8.
    """
    def __init__(self, repository: RepoType):
        self.repository = repository
