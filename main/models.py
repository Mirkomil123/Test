from django.db import models


# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
