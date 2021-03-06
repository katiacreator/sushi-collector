from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Add the Side_Dishes model
class Side(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  isVegan = models.BooleanField(default=False)
  isVegetarian = models.BooleanField(default=False)
  price = models.IntegerField(default=6)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sides_detail', kwargs={'pk': self.id})


class Sushi(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250, default='comes with free soy sauce, ginger, and wasabi paste')
  isVegan = models.BooleanField(default=False)
  isVegetarian = models.BooleanField(default=False)
  price = models.IntegerField(default=8)
  # includes = models.CharField(default=0)
    # Add the M:M relationship
  sides = models.ManyToManyField(Side)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sushi_detail', kwargs={'sushi_id': self.id})


