"""Imports from django"""
from django.contrib import admin
from django.urls import include, path

# Url links to project apps; home, services, stylists, bookings, accounts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('stylists/', include('stylists.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('allauth.urls')),
]
