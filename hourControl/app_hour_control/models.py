from django.db import models

class Projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    desc = models.TextField()
# Create your models here.
