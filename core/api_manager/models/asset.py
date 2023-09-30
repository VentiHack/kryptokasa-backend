from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nazwa aktywa")
    ticker = models.CharField(max_length=255,verbose_name="Ticker",primary_key=True)
    img_url = models.CharField(max_length=255,verbose_name="URL obrazka")

    def __str__(self):
        return f"{self.ticker} - {self.name}"

    class Meta:
        verbose_name = "Aktywo"
        verbose_name_plural = "Aktywa"
