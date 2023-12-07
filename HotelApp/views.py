from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tenants.utils import get_tenant_model
from django.contrib.auth.forms import UserCreationForm
from .forms import HotelForm
from .models import Hotel, HotelDomain
from django_tenants.utils import tenant_context
from django_tenants.utils import schema_context
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def my_index(request):
    tenant = get_tenant_model().objects.get(schema_name=request.tenant.schema_name)
    return render(request, 'index.html', {'hotel_name': tenant.name})


def my_gallery(request):
    return render(request,'gallery.html')

def my_about(request):
    return render(request,'about.html')

def my_booking(request):
    return render(request,'booking.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page, login page, or home page
            return redirect('my_index')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def create_tenant(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            with schema_context('public'):
                new_tenant = form.save()

                domain = form.cleaned_data['domain']
                new_domain = HotelDomain(domain=domain, tenant=new_tenant, is_primary=True)
                new_domain.save()

            return redirect('create_tenant.html') 
    else:
        form = HotelForm()

    return render(request, 'create_tenant.html', {'form': form})




def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Add validation for the fields

        # Create user
        user = User.objects.create_user(
            username=email, email=email, password=password,
            first_name=first_name, last_name=last_name
        )
        user.save()

        # Authenticate and login user
        new_user = authenticate(username=email, password=password)
        if new_user is not None:
            login(request, new_user)
            # Redirect to a success page, e.g., user's dashboard
            return redirect('dashboard')

    return render(request, 'register.html')