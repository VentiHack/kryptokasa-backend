from django.db import models


class Report(models.Model):
    nazwa_organu_egzekucyjnego = models.CharField(max_length=255, verbose_name="Nazwa organu egzakucyjnego")
    created = models.DateTimeField(auto_now=True)
    nr_sprawy = models.CharField(max_length=255, verbose_name="Numer sprawy")
    owner_data = models.CharField(max_length=255, verbose_name="Dane właściciela")

    def __str__(self):
        return f"Raport"

    class Meta:
        verbose_name = "Raport"
        verbose_name_plural = "Raport"
