from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def home(request):
   list_articles = Article.objects.all()
   context = {"liste_articles":list_articles}
   return render(request,"index.html",context)
def detail(request,id_article):
   article=Article.objects.get(id=id_article)
   category=article.category
   articles_en_relation=Article.objects.filter(category=category)
   return render(request,'detail.html',{"article":article,"aer":articles_en_relation})
   
def search(request):
   query=request.GET["article"]
   list_article= Article.objects.filter(title__contains=query)
   return render(request,"search.html", {"list_articles":list_article})