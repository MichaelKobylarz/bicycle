from django.urls import path

from rent.views import rent_view, hi_view

urlpatterns = [
    path('', rent_view),
    path('hi/', hi_view)

]