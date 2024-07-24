from django.urls import path

from rent.views import rent_view
urlpatterns = [
    path('main/', rent_view),

]