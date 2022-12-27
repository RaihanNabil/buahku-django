from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Kategori(models.Model):
    nama           = models.CharField(max_length=100)
    def __str__(self):
         return self.nama
     
    class Meta:
         verbose_name_plural = "Kategori"

class Produk(models.Model):
    nama   = models.CharField(max_length=100, null=True)
    kategori       = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    harga  = models.CharField(max_length=100, null=True)
    jumlah = models.CharField(max_length=100, null=True)
    image  = models.ImageField(null=True, blank=True)
    def __str__(self):
         return self.nama
     
    class Meta:
        verbose_name_plural = "Produk"
        
#Pelanggan     
class Customer(models.Model):
    User           = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nama           = models.CharField(max_length=100, null=True)
    alamat         = models.CharField(max_length=100, null=True)
    
#For The Order
class Order(models.Model):
    customer        = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered    = models.DateTimeField(auto_now_add=True)
    complete        = models.BooleanField(default=False,null=True,blank=False)
    transaksi_id    = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    produk         = models.ForeignKey(Produk, on_delete=models.SET_NULL, blank=True, null=True)
    order          = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity       = models.IntegerField(default=0, null=True, blank=True)
    date_added     = models.DateTimeField(auto_now_add=True)
    
class ShippingAddress(models.Model):
    customer       = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order          = models.ForeignKey(Order,    on_delete=models.SET_NULL, blank=True, null=True)
    address        = models.CharField(max_length=100, null=True)
    kota           = models.CharField(max_length=100, null=True)
    kodepos        = models.CharField(max_length=100, null=True)
    date_added     = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.address
    
class Buahh(models.Model):
    namabuah = models. CharField(max_length=100, blank=False, null=False)   
    jumlah      = models.CharField(max_length=50)
    harga       = models.CharField(max_length=50)
    kategori    = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date        = models.DateTimeField(auto_now_add=True) 
    image  = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.namabuah

    class Meta:
         verbose_name_plural = "buahh"