from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/', include('rent.urls')),

# def bike(x):
#     return HttpResponse("rent a bike")
]