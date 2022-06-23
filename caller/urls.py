from django.urls import path
from .views import get,add_comment,getComments,updatecustomerstate,logout_view,edit_comments,commentsFilter,getcommentdetails,updatecomment
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', get,name='callist'),
    path('add_comment',add_comment,name='add_comment'),
    path('choosecomcat',getComments,name='choosecomcat'),
    path('customerstate',updatecustomerstate,name='customerstate'),
    path('logout',logout_view,name='log_out'),
    path('editComments',edit_comments,name='edit_comments'),
    path('Com-filter',csrf_exempt(commentsFilter),name='getComFil'),
    path('Com-details',csrf_exempt(getcommentdetails),name='getComdetails'),
    path('Com-update',csrf_exempt(updatecomment),name='updatecoment'),
]

handler404 = 'caller.views.error_404_view'