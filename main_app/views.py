from django.shortcuts import render
from .models import Sushi, Side
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

class Home(LoginView):
  template_name = 'home.html'


def about(request):
  return render(request, 'about.html')

@login_required
def sushi_index(request):
  rolls = Sushi.objects.filter(user=request.user)
  return render(request, 'sushi/index.html', { 'rolls': rolls})

@login_required
def sushi_detail(request, sushi_id):
  sushi = Sushi.objects.get(id=sushi_id)
  return render(request, 'sushi/detail.html', { 'sushi': sushi })

class SushiCreate(LoginRequiredMixin, CreateView):
  model = Sushi
  fields = ['name', 'description', 'isVegan', 'isVegetarian', 'price']
    # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class SushiUpdate(LoginRequiredMixin,UpdateView):
  model = Sushi
  fields = ['name', 'description', 'isVegan', 'isVegetarian', 'price']

class SushiDelete(LoginRequiredMixin,DeleteView):
  model = Sushi
  success_url = '/sushi/'


@login_required
def sides_index(request):
  sides = Side.objects.all()
  return render(request, 'sides/index.html', { 'sides': sides})

@login_required
def sides_detail(request, side_id):
  side = Side.objects.get(id=side_id)
  return render(request, 'sides/detail.html', { 'side': side})

class SideCreate(LoginRequiredMixin,CreateView):
  model = Side
  fields = '__all__'

class SideList(LoginRequiredMixin,ListView):
  model = Side

class SideDetail(LoginRequiredMixin,DetailView):
  model = Side

class SideUpdate(LoginRequiredMixin,UpdateView):
  model = Side
  fields = ['name', 'description', 'isVegan', 'isVegetarian', 'price']

class SideDelete(LoginRequiredMixin,DeleteView):
  model = Side
  success_url = '/sides/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('sushi_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)