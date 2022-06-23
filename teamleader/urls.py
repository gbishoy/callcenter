from django.urls import path
from .views import get,workflowview,logout_view


urlpatterns = [
    path('plan',get,name='teamleader'),
    path('workflow',workflowview,name='workflow'),
    path('logout',logout_view,name='log_out'),
]
handler404 = 'teamleader.views.error_404_view'