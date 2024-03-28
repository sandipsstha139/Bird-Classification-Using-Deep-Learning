from django.urls import path
from home import views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.renderHome, name='renderHome'), 
    path('add_bird_species/', views.add_bird_species, name='add_bird_species'),  
    path('species_detail/<int:species_id>/', views.species_detail, name='species_detail'),
    path('about',views.about, name='about'),
]
