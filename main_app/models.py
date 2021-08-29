from django.db import models

# Create your models here.
class Sushi(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  price = models.IntegerField(default=0)
  
  