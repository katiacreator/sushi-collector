from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sushi/', views.sushi_index, name='sushi_index'),
  path('sushi/<int:sushi_id>', views.sushi_detail, name='sushi_detail'),
]