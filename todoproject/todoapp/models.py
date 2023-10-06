from django.db import models

# Create your models here.
class Task(models.Model):
    a=models.CharField(max_length=250)
    b=models.IntegerField()
    c=models.DateField()

    def __str__(self):
        return self.a