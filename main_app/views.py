from django.shortcuts import render
from .models import Sushi, Side
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from time import sleep
# import sys


# def typewriter():
#   sushi_words = 'California sushi roll cucumber avocado crab tuna nigiri delicious cucumber roll vegan vegetarian salmon nigiri salmon sushi  softshell crab' 
#   for letter in sushi_words:
#       sleep(0.08) # In seconds
#       sys.stdout.write(letter)
#       sys.stdout.flush()
      # return

# typewriter()-figure out where this should live to make it render on the home page

#define the home view
def home(request):
  return render(request, 'home.html')

#define the about view
def about(request):
  return render(request, 'about.html')

def sushi_index(request):
  rolls = Sushi.objects.all()
  return render(request, 'sushi/index.html', { 'rolls': rolls})

def sushi_detail(request, sushi_id):
  sushi = Sushi.objects.get(id=sushi_id)
  return render(request, 'sushi/detail.html', { 'sushi': sushi })

class SushiCreate(CreateView):
  model = Sushi
  fields = '__all__'

class SushiUpdate(UpdateView):
  model = Sushi
  fields = ['type', 'description', 'price']

class SushiDelete(DeleteView):
  model = Sushi
  success_url = '/sushi/'

# def additions_index(request, additions):
#   additions = Addition.objects.all()
#   return render(request, 'additions/index.html', { 'additions': additions})

#Side views begins here
def sides_index(request):
  sides = Side.objects.all()
  return render(request, 'sides/index.html', { 'sides': sides})

def sides_detail(request, side_id):
  side = Side.objects.get(id=side_id)
  return render(request, 'sides/detail.html', { 'side': side})

class SideCreate(CreateView):
  model = Side
  fields = '__all__'

"""
class SideUpdate(UpdateView):
  model = Side
  fields = ['isVegan', 'description', 'price']

class SideDelete(DeleteView):
  model = Side
  success_url = '/sides/' """