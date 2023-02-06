from django.db import models

from lib.models import TimestampedModel


class Department(TimestampedModel):
    name = models.CharField(verbose_name="Name department", max_length=32)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name
