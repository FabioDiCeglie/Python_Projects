from django.shortcuts import render
from django.http import HttpResponse
from django.views import View



# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog")

    def post(self,request):
        return HttpResponse("[POST]Welcome to my blog")




# def home(request):
#     if request.method == "GET":
#         return HttpResponse("Welcome to my blog")
#     if request.method == "POST":
#         return HttpResponse("POST BLOG")
