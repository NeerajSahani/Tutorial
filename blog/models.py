from django.db import models

# Create your models here.

class Basic(models.Model):
    field1 = models.CharField(max_length=100)
