from django.urls import path
from .views import my_index
from .views import my_gallery,my_about,my_booking,register,create_tenant,login_view, register_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', my_index, name='my_index'),
  path('gallery/', my_gallery, name='my_gallery'),
  path('about/', my_about, name='my_about'),
  path('booking/', my_booking, name='my_booking'),
  path('create_tenant/', create_tenant, name='create_tenant'),
  path('login/', login_view, name='login'),
  path('register/', register_view, name='register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




