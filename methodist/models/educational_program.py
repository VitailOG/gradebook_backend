from django.db import models

from lib.models import TimestampedModel


class EducationalProgram(TimestampedModel):
    name = models.CharField(verbose_name="Name educational programs", max_length=50, unique=True)

    department = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        verbose_name="Department",
        related_name="educational_programs"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Educational program"
        verbose_name_plural = "Educational programs"
