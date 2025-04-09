from django.shortcuts import redirect, render

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