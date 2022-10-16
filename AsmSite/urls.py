from django.urls import path

from AsmSite import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    # path('article/<slug:article_slug>', views.article, name='article'),
    # path('flags', views.flags, name='flags'),
]
