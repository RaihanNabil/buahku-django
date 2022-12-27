from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',        index,       name="index"),
    path('buah/',   buah,     name="buah"), 
    path("cart/",   cart,     name="cart"),
    path("login/",  login,    name="login"),
    path("signup/", signup,   name="signup"),
    path("logout/", logout_view,   name="logout"),
    path("checkout/",   checkout,     name="checkout"),
    path("dashboard/",   dashboard,     name="dashboard"),
    path("tabel_tambah/",   tabel_tambah,     name="tabel_tambah"),
    path("about/",   about,     name="about"),

    #apss here
    path('buah/', include('buah.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)