from django.shortcuts import render
from .models import Sushi

# Add the Sushi class & list and view function below the imports
# class Sushi:  # Note that parens are optional if not inheriting from another class
"""   def __init__(self, name, type, description, price):
    self.name = name
    self.type = type
    self.description = description
    self.price = price """

""" rolls = [
  Sushi('California', 'sushi roll', 'cucumber, avocado, and crab', 8),
  Sushi('Tuna', 'sashimi', 'delicious', 10),
  Sushi('Cucumber', 'sushi roll', 'vegan friendly', 4),
  Sushi('Salmon', 'nigiri', 'sustainably caught salmon', 8),
  Sushi('Captain Crunch Crab', 'sushi roll', 'epic, delicious treat, softshell crab battered in captain crunch batter and fried', 10)
] """

#define the home view
def home(request):
  return render(request, 'home.html')

#define the about view
def about(request):
  return render(request, 'about.html')

def sushi_index(request):
  rolls = Sushi.objects.all()
  return render(request, 'sushi/index.html', { 'rolls': rolls})
