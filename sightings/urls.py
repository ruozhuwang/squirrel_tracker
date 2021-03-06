from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.list_of_squirrels, name='list_of_squirrels'),
    path('stats', views.stats, name = 'stats'),
    path('add/', views.add_squirrel, name = 'add'),
    path('<str:squirrel_id>/', views.edit_squirrel, name='edit'),
]