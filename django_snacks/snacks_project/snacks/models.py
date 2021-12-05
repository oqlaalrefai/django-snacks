from django.db import models

# Create your models here.
class Thing(models.Model):
    '''create table of database called Thing'''
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title