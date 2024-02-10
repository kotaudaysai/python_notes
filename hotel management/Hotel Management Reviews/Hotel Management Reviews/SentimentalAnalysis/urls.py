from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from sentiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sentiapp.urls')),
]
