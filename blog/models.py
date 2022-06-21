from django.db import models


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    date = models.DateField(max_length=50)
    information = models.CharField(max_length=1000)
