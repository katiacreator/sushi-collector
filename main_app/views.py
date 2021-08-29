from django.shortcuts import render
from django.http import HttpResponse

#define the home view
def home(request):
  return HttpResponse('<h1>Hello Sushi Fans!</h1>')

#define the about view
def about(request):
  return render(request, 'about.html')

