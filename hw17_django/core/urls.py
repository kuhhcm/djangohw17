from django.contrib import admin
from django.urls import path
from app.views import IceCreamList, create_ice_cream

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IceCreamList.as_view(), name='home'),
    path('create/', create_ice_cream, name='create'),
]
