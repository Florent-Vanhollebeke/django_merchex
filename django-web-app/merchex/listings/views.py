from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch!</p>')


def listings(request):
    return HttpResponse('<h1>Liste des annonces pour les articles</h1><p>La liste arrive, patience!</p>')

def contact(request):
    return HttpResponse('<h1>Page de contact</h1><p>Nos coordonnées</p>')

