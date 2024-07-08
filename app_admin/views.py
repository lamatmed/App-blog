from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import *
from blog.forms import ArticleForm
def dashboard(request):
    return render(request,'db.html')
@login_required
def user_articles(request):
    if request.user.has_perm("blog.delete_article"):
        print('Il peut supprimer')
    else:
       print('Il ne peut pas  supprimer')
    return redirect ('dashboard')
    list_articles = Article.objects.filter(user =request.user)  
    return render(request,'my-articles.html', {'list_articles': list_articles})
# Create your views here.
class AddArticle(LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "add-article.html"
    success_url = "my-articles"
    
    def form_valid(self, form):
        form.instance.user =self.request.user
        return super().form_valid(form)
class updateArticle (LoginRequiredMixin,UpdateView):
     model = Article
     form_class  = ArticleForm
     template_name = "app_admin/article_form.html"
   
class deleteArticle (DeleteView):
     model = Article
     success_url = "/my-admin/my-articles"
    