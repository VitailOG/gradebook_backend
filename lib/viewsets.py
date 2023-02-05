from typing import Type

from django.db.models import Model
from rest_framework.serializers import SerializerMetaclass

from .repositories import BaseRepository


class SerializerMixin:
    serializers_map: dict[str, SerializerMetaclass] = {}

    def get_serializer_class(self) -> SerializerMetaclass:
        assert 'default' in self.serializers_map
        return self.serializers_map.get(getattr(self, 'action'), self.serializers_map['default'])


class RepositoryMixin:
    repositories_map: dict[str, Type[BaseRepository[Model]]] = {}

    @property
    def get_repository_class(self):
        assert 'default' in self.repositories_map
        return self.repositories_map.get(getattr(self, 'action'), self.repositories_map['default'])
