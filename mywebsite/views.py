from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    context = {
        'title':'Home',
        'heading':'selamat Datang',
    }
    return render(request,'index.html',context={'context':context})


def login(request):
    print(request)
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        print('this is adalah : ')
        usernames = request.POST['email']
        print('ini adalah ' + usernames)
        return redirect('bisa')
        # if form.is_valid():
        #     username = form.cleaned_data.get('email')
        #     print(username)
        # return redirect('login')