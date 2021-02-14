from django.shortcuts import render


# this view is like componements

#main lisitng page
def index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'lisitings/search.html')
