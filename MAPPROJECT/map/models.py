from ssl import cert_time_to_seconds
from statistics import mode
from django.db import models

# Create your models here.




class Search(models.Model):
    address=models.CharField(max_length=200, null=True)
    date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
