from django.db import models

ROLE_CHOICES = [
    ('admn', 'admin'),
    ('caja', 'caja'),
    ('mese', 'mesero'),
    ('clie', 'cliente'),
]

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=4, choices=ROLE_CHOICES) #admn, caja, mese
    
    def __str__(self):
        return self.username
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    