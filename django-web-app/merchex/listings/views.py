from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch!</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""<h1>Liste des annonces pour les articles</h1> 
                        <p>Ma petite liste!</p>
                        <ul>
                                <li>{listings[0].title}</li>
                                <li>{listings[1].title}</li>
                                <li>{listings[2].title}</li>
                        </ul>""")

def contact(request):
    return HttpResponse('<h1>Page de contact</h1><p>Nos coordonnées</p>')

