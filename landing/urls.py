from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('dictionary', views.dictionary, name='dictionary'),
    path('dictionary/<slug:term_slug>', views.dictionary_term, name='dictionary-term'),
]
