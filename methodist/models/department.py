from django.db import models


class Department(models.Model):
    """ Model Department """
    name = models.CharField(verbose_name="Name department", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
