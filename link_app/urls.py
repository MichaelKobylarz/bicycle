from django.urls import path
from link_app import views

urlpatterns = [
    path('first/', views.first_view, name='first'),
    path('second/', views.second_view, name='second'),
]