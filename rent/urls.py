from django.urls import path

from rent import views

urlpatterns = [
    # view bike
    path('', views.rent_view),

    # templates bike
    path('hi/', views.hi_view),
    path('hi2/', views.hi2_view),

    path('collection/', views.collection_view),
]