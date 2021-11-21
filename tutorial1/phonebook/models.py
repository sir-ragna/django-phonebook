
from django.db import models

# define objects that can be saved to the database

class PhoneRecord(models.Model):
    # id = models.BigAutoField(primary_key=True) 
    # ^ created automatically ==> see settings.py DEFAULT_AUTO_FIELD

    number = models.CharField(max_length=50)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name} ({self.number})"
    