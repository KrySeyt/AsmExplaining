from django.http import HttpRequest
from django.shortcuts import render


def flags(request: HttpRequest):
    return render(request, 'landing/flags.html')


def main(request: HttpRequest):
    return render(request, 'landing/main.html')
