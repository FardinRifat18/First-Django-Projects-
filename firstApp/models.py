
from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models. CharField(max_length=100, null=True, blank=True)
    roll = models. PositiveIntegerField()
    email = models.EmailField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='teacher/imange', default="def.jpg", null=True, blank=True)
    phone = models. IntegerField(default=0)
    address = models. CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f'{self.name}"s objest'
