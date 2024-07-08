from django.urls import path
from .views import *
urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('my-articles',user_articles,name='my-articles'),
    path('ajouter-article',AddArticle.as_view(),name='ajouter-article'),
    path('update-article/<int:pk>',updateArticle.as_view(),name='update-article'),
    path('delete-article/<int:pk>',deleteArticle.as_view(),name='delete-article'),
]