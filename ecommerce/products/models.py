from django.db import models

# Create your models here.
class Product(models.Model):
    title           = models.Charfield(max_lenght=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=0)