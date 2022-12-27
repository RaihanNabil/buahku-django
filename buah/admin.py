from django.contrib import admin
from buah.models import *

# Register your models here.
admin.site.register(Kategori)

#1
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama','kategori','harga','jumlah','image')
admin.site.register(Produk, ProdukAdmin)
    
#2
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('nama','alamat')
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class BuahhAdmin(admin.ModelAdmin):
    list_display = ('namabuah','jumlah','harga','kategori','date','image')
admin.site.register(Buahh, BuahhAdmin)