from django.shortcuts import render, redirect, get_object_or_404
from .models import MyDiary
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_view(request):
    entries = MyDiary.objects.filter(user=request.user)
    context = {'entries' : entries}
    return render(request, 'mydiary/home.html', context)

@login_required
def add_entry_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            MyDiary.objects.create(user = request.user, title=title, content=content)
            
            messages.success(request, "The Data add success")
            return redirect('home')
        else:
            messages.error(request, "Please fill fiedl properly")
            
    return render(request, 'mydiary/add_entry.html')

@login_required
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, "The both password not match")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "The Username Alreday Present in the Database")
            return redirect('register')
        
        User.objects.create_user(username=username, password=password)
        messages.success(request, "The registration success")
        return redirect('login')
    return render(request, 'mydiary/register.html')

@login_required
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "The Login successfull")
            return redirect('home')
        else:
            messages.error(request, "The credentials in not valid")
            
    return render(request, 'mydiary/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "The user Logout success")
    return redirect('login')

@login_required
def delete_entry_view(request, entry_id):
    entry = get_object_or_404(MyDiary, id=entry_id, user=request.user)    
    entry.delete()
    messages.success(request, "The Entry is deleted success")
    return redirect('home')
    