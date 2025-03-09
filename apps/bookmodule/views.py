from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/html5/links.html')

def formatting(request):
    return render(request, 'bookmodule/html5/formatting.html')
 
    
def listing(request):
    return render(request, 'bookmodule/html5/listing.html')
 
    
def table(request):
    return render(request, 'bookmodule/html5/table.html')
 
