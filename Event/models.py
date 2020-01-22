from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"

    user = models.ForeignKey(User,
                             verbose_name="Użytkownik",
                             on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nazwa",
                            max_length=150,
                            null=False,
                            blank=False)
    description = models.TextField(verbose_name="Opis",
                                   max_length=5000,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.name


QUESTION_TYPE_CHOICES =(
    (1, "Otwarte"),
    (2, "Zamknięte")

)


class Question(models.Model):
    class Meta:
        verbose_name = "Pytanie"
        verbose_name_plural = "Pytania"

    event = models.ForeignKey(Event,
                              verbose_name="Wydarzenie",
                              on_delete=models.CASCADE)
    q_type = models.IntegerField(verbose_name="Rodzaj pytania",
                                 choices=QUESTION_TYPE_CHOICES)
    name = models.CharField(verbose_name="Nazwa",
                            max_length=150,
                            null=False,
                            blank=False)
    description = models.TextField(verbose_name="Opis",
                                   max_length=5000,
                                   null=True,
                                   blank=True)


class Answer(models.Model):
    class Meta:
        verbose_name = "Odpowiedź"
        verbose_name_plural = "Odpowiedzi"

    event = models.ForeignKey(Event,
                              verbose_name="Wydarzenie",
                              on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             verbose_name="Użytkownik",
                             on_delete=models.CASCADE)

    first_name = models.CharField(verbose_name="Imie",
                                  max_length=50)
    answers = models.TextField(verbose_name="Odpowiedzi")
    created = models.DateTimeField(verbose_name="Utworzony",
                                   auto_now_add=True)