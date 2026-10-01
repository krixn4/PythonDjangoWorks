from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# #function based
# def Home(request):
#     if (request.method=="GET"):
#         return HttpResponse("Welcome to Django")
#
# #define an index view returns index page
#
# def Index(request):
#     if(request.method=="GET"):
#         return HttpResponse("Index Page")

from django.views import View
class Home(View):
    def get(self,request):
        return HttpResponse("Welcome to Django")

class Index(View):
    def get(self,request):
        return HttpResponse("Welcome to Django")