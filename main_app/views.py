from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#define the home view
def home(request):
  return HttpResponse('<h1>Hello Sushi Fans!</h1>')

#define the about view
def about(request):
  return HttpResponse('<h1>About Sushi</h1>')

