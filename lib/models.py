from django.db import models
from behaviors.behaviors import Timestamped


class TimestampedModel(Timestamped):

    class TimestampedQuerySet(models.QuerySet[models.Model]):

        def modified(self) -> models.QuerySet[models.Model]:
            return self.filter(modified__isnull=False)

        def limit(self, limit: int) -> models.QuerySet[models.Model]:
            return self.all()[:limit]

        def offset(self, offset: int) -> models.QuerySet[models.Model]:
            return self.all()[offset:]

    objects = TimestampedQuerySet.as_manager()

    class Meta:
        abstract = True
