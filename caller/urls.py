from django.urls import path
from .views import get,add_comment,getComments,updatecustomerstate

urlpatterns = [
    path('', get,name='callist'),
    path('add_comment',add_comment,name='add_comment'),
    path('choosecomcat',getComments,name='choosecomcat'),
    path('customerstate',updatecustomerstate,name='customerstate'),
]

handler404 = 'caller.views.error_404_view'