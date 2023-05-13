from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Task, User

def dashboard(request):
    if 'user_id' in request.session:
        user = User.objects.filter(id=request.session['user_id']).first()
        tasks = Task.objects.filter(user=user)
        return render(request, 'dashboard/index.html', {'tasks': tasks, 'user': user})
    else:
        return HttpResponse('Para acessar o dashboard é necessário realizar o login')

def create_task(request):
    if 'user_id' in request.session:
        user = User.objects.filter(id=request.session['user_id']).first()
        
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            category = request.POST['priority']
            
            task = Task(user=user, title=title, description=description, category=category, status='pendete')
            task.save()
            return redirect('dashboard')
        else:
            return render(request, 'dashboard/create_task.html')
    else:
        return HttpResponse('Para acessar o dashboard é necessaŕio realizar o login')

def update_task(request, task_id):
    if 'user_id' in request.session:
        user = User.objects.filter(id=request.session['user_id']).first()
        task = Task.objects.filter(id=task_id, user=user).first()
        
        if request.method == 'POST':
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.category = request.POST['priority']
            task.save()
            return redirect('dashboard')
        else:
            return render(request, 'dashboard/update_task.html', {'task': task})
    else:
        HttpResponse('Para acessar o dashboard é necessário realizar o login')

def delete_task(request, task_id):
    if 'user_id' in request.session:
        task = get_object_or_404(Task, id=task_id)
        if request.method == 'POST':
            user_confirm = request.POST['user_confirm']
            if user_confirm == 'on' and user_confirm is not None:
                task.delete()
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            return render(request, 'dashboard/delete_task.html', {'task': task})
    else:
        return HttpResponse('Para acessar o dashboard é necessário realizar o login')