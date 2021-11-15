from django.db import models
from django.db.models.base import Model

# Create your models here.

class Drug(models.Model):
    drug=models.CharField(max_length=255)
    compony=models.CharField(max_length=255)

    def __str__(self):
        return self.drug