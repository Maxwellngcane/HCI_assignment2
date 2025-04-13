from django.urls import path # type: ignore
from .views import home_view, task_create_view, wellness_check_view, login_view, resources_view, campus_view, register_view, schedule_view, about_view



urlpatterns = [
    path('', login_view , name='login' ),
    path('register', register_view , name='register' ),
    path('home', home_view, name='home'),
    path('task_create/', task_create_view, name='task_create'), 
    path('wellness/check-in/', wellness_check_view, name='wellness_check'),
    path('view_schedule', schedule_view , name='view_schedule' ),
    path('resources/', resources_view, name='resources'), 
    path('campus-life/', campus_view, name='campus-life'), 
    path('about/', about_view, name='about'), 

    
]