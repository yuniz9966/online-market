from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField(max_length=75,unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name