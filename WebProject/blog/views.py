# from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# def home(request):
#     if request.method == "GET":
#         return HttpResponse("Welcome to my blog")
#     if request.method == "POST":
#         return HttpResponse("POST BLOG")

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog")

    def post(self,request):
        return HttpResponse("[POST]Welcome to my blog")


class Article(View):
    def get(self, request):
        articles = [
{
"title": "Python 5 is officially announced",
"category": "tech",
"author": "Guido van Rossum",
"content": "Just joking, we will have Python 3 for some years",
"creation_date": datetime.now()
},
{
"title": "Tesla goes bankrupt",
"category": "auto",
"author": "Elon Musk",
"content": "Just trying to increase tesla share price here!",
"created_at": datetime.now()
}
]

        return render(request, "articles.html", {"articles": articles})





