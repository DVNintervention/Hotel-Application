# Hotel/views.py

from django.shortcuts import render

def my_index(request):
    return render(request, 'index.html')

def my_gallery(request):
    return render(request, 'gallery.html')

def my_booking(request):
    return render(request, 'booking.html')