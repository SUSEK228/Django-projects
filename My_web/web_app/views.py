from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Task
from . forms import TaskForm

# Create your views here.
def main(request):
    return render(request, 'main.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, ' User does not exist')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info('This username is already use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        messages.info(request, 'Your passwords are not the same')
        return redirect('register')
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def todo(request):
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')
    
    context = {'tasks': tasks, 'TaskForm' : form}
    return render(request, 'todo.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')
    context = {'TaskForm' : form}
    return render(request, 'update_task.html', context)

def delete_task(request, pk):
    task= Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('todo')
    context = {'task': task}
    return render(request, 'delete_task.html', context)
