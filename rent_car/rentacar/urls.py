from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('reviews', views.reviews, name='reviews'),
    path('cars', views.cars, name='cars'),
    path('accept', views.accept, name='accept'),
    path('message', views.message, name='message'),
    path('new-order', views.new_order, name='new_order'),
    path('email', views.sendanemail, name='email'),
]
