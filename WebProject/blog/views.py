# from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,redirect
from blog.models import ArticleModel
from django.utils import timezone
from blog.forms import ArticleForm


# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog")

    def post(self,request):
        return HttpResponse("[POST]Welcome to my blog")


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()
        return render(request, "articles.html", {"articles": articles, "form": ArticleForm()})

    def post(self, request):
        # title = request.POST["title"]
        # category = request.POST["category"]
        # author = request.POST["author"]
        # content = request.POST["content"]
        # articles = ArticleModel.objects.create(title =title,category=category,author=author,content=content, createdAt= datetime.now(tz=timezone.utc))
        form = ArticleForm(request.POST)
        form.instance.createdAt = datetime.now(tz=timezone.utc)
        form.save()
        return redirect("/blog/articles")



