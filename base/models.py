from django.db import models

# Create your models here.

class receipe(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="shop/images")
    