from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sushi/', views.sushi_index, name='sushi_index'),
  path('sushi/<int:sushi_id>', views.sushi_detail, name='sushi_detail'),
  path('sushi/create/', views.SushiCreate.as_view(), name='sushi_create'),
  path('sushi/<int:pk>/update/', views.SushiUpdate.as_view(), name='sushi_update'),
  path('sushi/<int:pk>/delete/', views.SushiDelete.as_view(), name='sushi_delete'),
]