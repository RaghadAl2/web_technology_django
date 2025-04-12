from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .models import Address
from .models import Student
from django.db.models import Q, Count, Min, Max, Sum, Avg
def index(request):
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()
    return render(request, "bookmodule/index.html")
 
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
   
def lab8_task1(request):
    mybooks=Book.objects.filter(Q(price__lte=80))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')  
       
def lab8_task2(request):
    mybooks=Book.objects.filter(Q(edition__gte=3)&(Q(title__icontains="co")|Q(author__icontains="co")))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')  
    
         
def lab8_task3(request):
    mybooks=Book.objects.filter(~Q(edition__gte=2)&(~Q(title__icontains="ll")|~Q(author__icontains="co")))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')  
     
         
def lab8_task4(request):
    mybooks=Book.objects.all().order_by('title')
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')  
      
          
def lab8_task5(request):
    query = Book.objects.aggregate(
    count=Count('id'),
    total=Sum('price', default=0),
    average=Avg('price',default=0),
    max=Max('price',default=0) ,
    min=Min('price',default=0) ,
    )

    return render(request, 'bookmodule/books_info.html',{'query':query})



def lab8_task7(request):
    query = Student.objects.values('address__city').annotate(total=Count('id'))
    return render(request, 'bookmodule/Student_list.html',{'query':query})

      
      
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1,book2,book3]
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request, 'bookmodule/search.html')
