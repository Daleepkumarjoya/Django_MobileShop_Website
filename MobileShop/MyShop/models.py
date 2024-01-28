from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Product(models.Model):
    Product_id = models.AutoField
    Product_Image = models.ImageField(upload_to="images")
    Product_Name = models.CharField(max_length=200)
    Product_Price = models.IntegerField(default=0)
    Product_Desc = models.TextField()
    # new_slug = AutoSlugField(populate_from='Product_Name', unique=True, null=True, default=None)

    def __str__(self):
        return self.Product_Name


class contact(models.Model):
    id = models.AutoField
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    number = models.IntegerField(default=0)
    query = models.TextField()

    def __str__(self):
        return self.Name


class Orders(models.Model):
    id = models.AutoField(primary_key=True, default=None, blank=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    number = models.IntegerField(default=0)
    Address = models.TextField()

    def __str__(self):
        return self.Name





