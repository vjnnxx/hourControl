from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=30)
    desc = models.TextField()
# Create your models here.
