# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from buah.models import *
from django.contrib.auth.decorators import login_required



def index(request):
    template_name = 'front/index.html'
    return render(request, template_name)

@login_required
def buah(request):
    template_name = 'front/buah.html'
    produk = Produk.objects.all()
    context = {
        'produk' : produk
        }
    return render(request,template_name,context)

def login(request):
    template_name = 'akun/login.html'
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            # datanya ada 
            print('username anda benar')
            auth_login(request,user)
            return redirect('buah')
        else:
            # data anda gk ada 
            print('username anda salah')
    context  = {
        'title' : 'form-login'
    }
    return render(request, template_name,context)

@login_required
def cart(request):
    template_name ='front/cart.html'
    return render(request,template_name)
def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    template_name='akun/signup.html'
    return render(request,template_name)

@login_required
def checkout(request):
    template_name='front/checkout.html'
    return render(request,template_name)

def dashboard(request):
    template_name   = "back/dashboard.html"
    context         = {
        'title'     : 'dashboard'
    }
    return render (request, template_name,context)

def tabel_tambah(request):
    template_name   = "back/tabel_tambah.html"
    context         = {
        'title'     : 'dashboard'
    }
    return render (request, template_name,context)

@login_required
def about(request):
    template_name ='front/about.html'
    return render(request,template_name)