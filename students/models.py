from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)  
    email = models.EmailField(unique=True, blank=False)  
    phone = models.CharField(max_length=15, blank=False)  
    course = models.CharField(max_length=100, blank=False)  

    def __str__(self):
        return self.name
