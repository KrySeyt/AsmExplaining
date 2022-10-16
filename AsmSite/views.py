from django.http import HttpRequest
from django.shortcuts import render


# def flags(request: HttpRequest):
#     return render(request, 'AsmSite/flags.html')
#
#
# def main(request: HttpRequest):
#     return render(request, 'AsmSite/main.html')


def articles_list(request: HttpRequest):
    return render(request, 'AsmSite/articles_list.html')
