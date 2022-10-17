from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class LawsDB(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=800,default='')