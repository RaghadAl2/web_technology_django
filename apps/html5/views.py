from django.shortcuts import render

# Create your views here.

def links(request):
    return render(request, 'html5/links.html')

def formatting(request):
    return render(request, 'html5/formatting.html')
 
    
def listing(request):
    return render(request, 'html5/listing.html')
 
    
def table(request):
    return render(request, 'html5/table.html')
 
