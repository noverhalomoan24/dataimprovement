#from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='items'),
    path('salerystatic',views.view_salery,name='salerystatic'),
]

