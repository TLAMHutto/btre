from django.shortcuts import render
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listings(request):
    return render(request, 'listings/listings.html')

def search(request):
    return render(request, 'listings/search.html')
