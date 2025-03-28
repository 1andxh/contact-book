from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True, null=False)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} added to contacts."
    
    