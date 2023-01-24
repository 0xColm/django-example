from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('index/', views.index),
    path('show/', views.show),
    path('template/', views.template),
]