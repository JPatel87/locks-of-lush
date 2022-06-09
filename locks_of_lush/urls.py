from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('stylists/', include('stylists.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('allauth.urls')),
]
