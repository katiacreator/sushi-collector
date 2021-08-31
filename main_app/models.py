from django.db import models
from django.urls import reverse

# Create your models here.
class Sushi(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  price = models.IntegerField(default=0)
  # includes = models.CharField(default=0)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sushi_detail', kwargs={'sushi_id': self.id})

# Add the Side_Dishes model
class Side(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  isVegan = models.BooleanField(default=False)
  price = models.IntegerField(default=0)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sides_detail', kwargs={'pk': self.id})