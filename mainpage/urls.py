from django.urls import path
from .views import loginpageview,homepage

urlpatterns=[
    path('',loginpageview,name='loginpage'),
    path('home',homepage,name='homepage'),
]
