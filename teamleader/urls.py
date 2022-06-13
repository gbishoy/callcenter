from django.urls import path
from .views import get,workflowview


urlpatterns = [
    path('plan',get,name='teamleader'),
    path('workflow',workflowview,name='workflow'),
]
handler404 = 'teamleader.views.error_404_view'