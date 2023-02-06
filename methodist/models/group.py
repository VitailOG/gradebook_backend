from django.db import models

from lib.models import TimestampedModel


class Group(TimestampedModel):
    name = models.CharField(verbose_name="Name group", max_length=15, unique=True)

    educational_program = models.ForeignKey(
        'EducationalProgram',
        verbose_name="Education Program",
        on_delete=models.CASCADE,
        related_name='groups'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
