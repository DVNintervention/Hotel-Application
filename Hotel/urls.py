"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django import views
from django.urls import include, path
from HotelApp.views import my_index
from HotelApp.views import my_gallery,my_about,my_booking


urlpatterns = [
     path('', my_index, name='my_index'),
     path('gallery.html/', my_gallery, name='my_gallery'),
     path('about.html/', my_about, name='my_about'),
     path('booking.html/', my_booking, name='my_booking'),
     path('admin/', admin.site.urls),
     path('HotelApp/', include('HotelApp.urls')),

]
