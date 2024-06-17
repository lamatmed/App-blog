from django.urls import path
from . import views
urlpatterns=[
    
     path('', views.home,name="home"),
    path('article/<int:id_article>',views.detail,name="detail")
]
