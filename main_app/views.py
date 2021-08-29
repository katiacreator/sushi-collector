from django.shortcuts import render
from django.http import HttpResponse

# Add the Sushi class & list and view function below the imports
class Sushi:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, price):
    self.name = name
    self.type = type
    self.description = description
    self.price = price

sushi_list = [
  Sushi('California', 'sushi roll', 'cucumber, avocado, and crab', 8),
  Sushi('Tuna', 'sashimi', 'delicious', 10),
  Sushi('Cucumber', 'sushi roll', 'vegan friendly', 4),
  Sushi('Salmon', 'nigiri', 'sustainably caught salmon', 8),
  Sushi('Captain Crunch Crab', 'sushi roll', 'epic, delicious treat, softshell crab battered in captain crunch batter and fried', 10)
]

#define the home view
def home(request):
  return HttpResponse('<h1>Hello Sushi Fans!</h1>')

#define the about view
def about(request):
  return render(request, 'about.html')

def sushi_index(request):
  return render(request, 'sushi/index.html', { 'sushi_list': sushi_list })
