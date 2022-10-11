from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Template, RequestContext
from django.template.loader import render_to_string
from django.utils.safestring import SafeString

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
    template_str: SafeString = render_to_string(request=request, template_name='landing/term.html', context=context)
    context: RequestContext = RequestContext(request, context)
    template: Template = Template(template_str)
    return HttpResponse(template.render(context))

