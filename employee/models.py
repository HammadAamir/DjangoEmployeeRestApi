from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} joined on {self.date_joined}"