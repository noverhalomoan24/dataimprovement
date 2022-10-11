from django.shortcuts import render,redirect
from django.views.generic import View
import io,json,os
from django.contrib import messages
from django.http import JsonResponse,HttpResponse

# Create your views here.

# SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
#
# print(SETTINGS_PATH)
# TEMPLATE_DIRS = (
#     os.path.join(SETTINGS_PATH, 'templates'),
# )


if os.path.isfile('D:\Python\Database_Test\portfolio\Games\templates\say.html'):
    print('Saya')

def gamesss(request):
    return render(request,'games.html')