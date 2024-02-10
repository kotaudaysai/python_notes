from django.contrib import admin
from django.urls import path
from sentiapp import views
app_name='sentiapp'
urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('review/', views.review, name='review'),
    path('fake/', views.fake, name='fake'),
    path('normal/', views.normal, name='normal'),
    path('cls/', views.clas, name='clas')
]

