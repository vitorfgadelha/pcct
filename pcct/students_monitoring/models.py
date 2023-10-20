from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField('Name', max_length=200, null=False)
    registration = models.CharField('Registration',max_length=50, null=False)