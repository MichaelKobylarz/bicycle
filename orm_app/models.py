from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=64)

def str(self):
    return "{self.name}"

class Country(models.Model):
    name = models.CharField(max_length=64)
    capitol = models.OneToOneField('Capital', on_delete=models.CASCADE)

class Capital(models.Model):
    name = models.CharField(max_length=64)