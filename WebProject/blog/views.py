# from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from blog.models import ArticleModel


# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog")

    def post(self,request):
        return HttpResponse("[POST]Welcome to my blog")


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, "articles.html", {"articles": articles})





