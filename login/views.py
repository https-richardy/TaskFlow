from django.shortcuts import render, redirect, HttpResponse
from dashboard.models import User

def main(request):
    return render(request, 'auth/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).first()
        if user is not None:
            request.session['user_id'] = str(user.id)
            return redirect('dashboard')
        else:
            return render(request, 'auth/error.html')
    else:
        return render(request, 'auth/login.html')

def create_account(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return render(request, 'auth/account_exists.html')
        else:
            user = User(name=name, email=email, password=password)
            user.save()
            return render(request, 'auth/account_created.html', {'user': user})
    return render(request, 'auth/sign_up.html')