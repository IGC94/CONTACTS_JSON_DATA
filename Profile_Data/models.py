from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    Email = models.EmailField()

    def __str__(self):
        return self.full_name
