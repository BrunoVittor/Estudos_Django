from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    creation = models.DateTimeField(auto_now=True)
