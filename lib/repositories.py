from typing import TypeVar, Generic

from django.db.models import Model

T = TypeVar('T', bound=Model)


class BaseRepository(Generic[T]):
    model: T | None = None
