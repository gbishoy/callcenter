from django.urls import path
from .views import loginpageview,homepage,logout_view

urlpatterns=[
    path('',loginpageview,name='loginpage'),
    path('home',homepage,name='homepage'),
    path('logout',logout_view,name='log_out'),
    
]
handler404 = 'mainpage.views.error_404_view'