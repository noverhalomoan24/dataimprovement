#from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index),
    path('download_pdf',views.DownloadPDF.as_view(),name="download_pdf"),
]

