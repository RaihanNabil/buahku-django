from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required,  user_passes_test


def is_administrator(user):
    if user.groups.filter(name='Administrator').exists():
        return True
    else:
        return False
    
def dashboard(request):
    if request.user.groups.filter(name='Administrator').exists():
        request.session['is_administrator'] = 'administrator'
    template_name   = "back/dashboard.html"
    context         = {
        'title'     : 'dashboard'
    }
    return render (request, template_name,context)

@login_required
@user_passes_test(is_administrator)
def buah_list(request):
    template_name = 'back/buah_list.html'
    produk_list = Produk.objects.all()
    context = {
        'title':'my home',
        'produk':produk_list
    }
    return render(request, template_name, context)

def buah_add(request):
    template_name = 'back/buah_add.html'
    kategori = Kategori.objects.all()
    
    if request.method == "POST":
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_harga  = request.POST.get('harga')
        input_jumlah = request.POST.get('jumlah')
        
        #input Kategori Dulu
        get_kategori = Kategori.objects.get(nama=input_kategori)

        #simpan produk karena ada relasi ke tabel kategori 
        Produk.objects.create(
            nama           = input_nama,
            kategori       = get_kategori,
            harga          = input_harga,
            jumlah         = input_jumlah,        
        )
        return redirect(buah_list)
    context = {
        'title':'my home',
        'kategori':kategori
    }
    return render(request, template_name, context)

def buah_update(request ,id ):
    template_name = 'back/buah_add.html'
    kategori = Kategori.objects.all()
    get_produk = Produk.objects.get(id=id)
    if request.method == "POST":
        
        input_kategori  = request.POST.get('kategori')
        input_nama      = request.POST.get('nama')

        #input Kategori Dulu
        get_kategori    = Kategori.objects.get(nama=input_kategori)
        #simpan produk karena ada relasi ke tabel kategori 
        get_produk.nama   = input_nama
        get_produk.harga  = input_nama
        get_produk.jumlah = input_nama
        get_produk.kategori = get_kategori
        get_produk.save() 
        return redirect(buah_list)
    context = {
        'title':'my home',
        'kategori'   :kategori,
        'get_produk' : get_produk,
    }
    return render(request, template_name, context)
def buah_delete(request,id ):
    Produk.objects.get(id=id).delete()
    return redirect(buah_list)  

def buahh(request):
    
    template_name = "back/tabel_buah.html"
    produk = Produk.objects.all()
    buahh = Buahh.objects.all()
    for p in buahh:
        print(p)
    context       = {
        'title'   : 'tabel_buah',
        'buahh'   : buahh,  
        'produk'  : produk,
    }
    return render (request, template_name, context)

def user(request):
    template_name   = "back/tabel_user.html"
    context         = {
        'title' : 'tabel_user'
    }
    return render (request, template_name, context)
