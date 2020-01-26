from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"

    user = models.ForeignKey(User,
                             verbose_name="Użytkownik",
                             on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nazwa Wydarzenia",
                            max_length=150,
                            null=False,
                            blank=False)
    description = models.TextField(verbose_name="Opis Wydarzenia",
                                   max_length=2000,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.name
