from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('article/<int:article_pk>', views.show_article, name='article'),
]
