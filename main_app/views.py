from django.shortcuts import redirect, render
from .models import Sushi, Side
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
  # Get the sides the sushi doesn't have
  sides_sushi_doesnt_have = Side.objects.exclude(id__in = sushi.sides.all().values_list('id'))
  return render(request, 'sushi/detail.html', {
    # Add the sides to be displayed
    'sushi': sushi, 'sides': sides_sushi_doesnt_have
  })

class SushiCreate(LoginRequiredMixin, CreateView):
  model = Sushi
  fields = ['name', 'description', 'isVegan', 'isVegetarian', 'price']
    # This inherited method is called when a
  # valid sushi form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the sushi
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

def add_side(request, sushi_id, side_id):
  Sushi.objects.get(id=sushi_id).sides.add(side_id)
  return redirect('sushi_detail', sushi_id=sushi_id)

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