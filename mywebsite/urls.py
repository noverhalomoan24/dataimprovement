
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Blog/',include('Blog.urls')),
    path('items/',include('Items.urls')),
    path('Games/',include('Games.urls')),
    path('service/',include('Layanan.urls')),
    path('',views.index,name='index'),
    # path('login/',views.login,name='login'),
    # path('bisa/',views.login,name='bisa'),
]
