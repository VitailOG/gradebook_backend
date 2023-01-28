from django.db import models


class Permission(models.Model):  # todo django permission
    """ Permissions for users """
    name = models.CharField(verbose_name="Право доступу", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Право доступу"
        verbose_name_plural = "Права доступу"
