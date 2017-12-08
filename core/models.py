from django.db import models

class Transactions(models.Model):
    name = models.CharField(max_length=200)
    sum = models.FloatField()
    note = models.TextField()

def __unicode__(self):
    return self.name

def __str__(self):
    return self.name

def __unicode__(self):
    return self.note

def __str__(self):
    return self.note