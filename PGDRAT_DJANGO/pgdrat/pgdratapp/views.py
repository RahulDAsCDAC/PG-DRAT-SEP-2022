from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from pgdratapp.models import Task
from pgdratapp.forms import TaskForm
from django.contrib import messages

# CRUD = Create Read Update Delete

# Create your views here.
def home(request):
    return render(request, "index.html")

def addTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Display Task')
    context = {"form":form}
    return render(request, "addtask.html", context=context)

def displayTask(request):
    task = Task.objects.all()
    context = {"tasks":task}
    return render(request, "displaytask.html", context=context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Display Task')
    context = {'form':form}
    return render(request, "updatetask.html", context=context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("Display Task")
    context = {'task':task}
    return render(request, "deletetask.html", context=context)

def signIn(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('Log In')
    context = {"form":form}
    return render(request, "signin.html", context=context)

def logIn(request):
    if request.user.is_authenticated:
        return redirect("Home")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, "Welcome, {username}")
                    return redirect("Home")
                else:
                    messages.error(request, "Username or Password is wrong")
            else:
                messages.error(request, "Username or Password is wrong")
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, "login.html", context=context)

def logOut(request):
    logout(request)
    return redirect("Log In")