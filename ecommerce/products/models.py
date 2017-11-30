from django.db import models

import random
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def featured(self):
        return self.filter(featured=True, active=True)


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_query().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_queryset(self):
        return ProductQuerySet(models.query.QuerySet)

    def all(self):
        return self.get_queryset().active()

     def featured(self):
        return self.get_queryset().featured()


class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active          = models.BooleanField(default=True)
    featured        = models.BooleanField(default=False)

    objects = ProductManager()
    
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title