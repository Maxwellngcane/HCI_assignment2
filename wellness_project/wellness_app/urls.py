from django.urls import path
from .views import home_view, task_create_view, wellness_check_view


urlpatterns = [
    path('', home_view, name='home'),
    path('task_create/', task_create_view, name='task_create'), 
    path('wellness/check-in/', wellness_check_view, name='wellness_check'),
]