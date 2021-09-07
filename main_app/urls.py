from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('sushi/', views.sushi_index, name='sushi_index'),
  path('sushi/<int:sushi_id>', views.sushi_detail, name='sushi_detail'),
  path('sushi/create/', views.SushiCreate.as_view(), name='sushi_create'),
  path('sushi/<int:pk>/update/', views.SushiUpdate.as_view(), name='sushi_update'),
  path('sushi/<int:pk>/delete/', views.SushiDelete.as_view(), name='sushi_delete'),

  #Side routes begins here
  path('sides/', views.sides_index, name='sides_index'),
  path('sides/create/', views.SideCreate.as_view(), name='sides_create'),
  path('sides/<int:pk>/', views.SideDetail.as_view(), name='sides_detail'),
  path('sides/<int:pk>/update', views.SideUpdate.as_view(), name='side_update'),
  path('sides/<int:pk>/delete', views.SideDelete.as_view(), name='side_delete'),

  #associate side dishe with a sushi
  path('sushi/<int:sushi_id>/add_side/<int:side_id>/', views.add_side, name='add_side'),
  #Signup routes start here
  path('accounts/signup/', views.signup, name='signup'),
]