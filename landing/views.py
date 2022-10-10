from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import render

from .models import DictionaryTerm


def main(request: HttpRequest):
    return render(request, 'landing/main.html')


def dictionary(request: HttpRequest):
    terms: QuerySet = DictionaryTerm.objects.all()

    context: dict = {
        'terms': terms,
    }
    return render(request, 'landing/dictionary.html', context)


def dictionary_term(request: HttpRequest, term_slug: str):
    term = DictionaryTerm.objects.get(slug=term_slug)

    context: dict = {
        'term': term,
    }
    return render(request, 'landing/term.html', context)
