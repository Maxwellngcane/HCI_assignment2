from django.shortcuts import redirect, render # type: ignore

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

def task_create_view(request):
    if request.method == 'POST':
        # Process form data (would normally save to database)
        return redirect('home')
    return render(request, 'task_form.html')

def wellness_check_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'wellness_check.html')

def schedule_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'view_schedule.html')

def login_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'register.html')

def resources_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'resources.html')

def campus_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'campus_life.html')

def about_view(request):
    if request.method == 'POST':
        # Process wellness data
        return redirect('home')
    return render(request, 'about.html')