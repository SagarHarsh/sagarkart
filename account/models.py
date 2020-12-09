from django.db import models

# Create your models here.

class College(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    contact=models.BigIntegerField()

    def __str__(self):

        return self.name
