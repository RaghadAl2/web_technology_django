from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .models import Address
from .models import Student
from django.db.models import Q, Count, Min, Max, Sum, Avg
from .forms import BookForm

def index(request):
    Books=Book.objects.all()
    return render(request, "bookmodule/listbooks.html",{'Books':Books})
 
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
        return render(request, 'bookmodule/index.html',{'message':'All the Prices are higher than 80'})  
       
def lab8_task2(request):
    mybooks=Book.objects.filter(Q(edition__gte=3)&(Q(title__icontains="co")|Q(author__icontains="co")))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'There is no elements to display'})  
    
         
def lab8_task3(request):
    mybooks=Book.objects.filter(~Q(edition__gte=2)&(~Q(title__icontains="ll")|~Q(author__icontains="co")))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'There is no elements to display'})  
     
         
def lab8_task4(request):
    mybooks=Book.objects.all().order_by('title')
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'There is no elements to display'})  
      
          
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


def lab10_part1_listbook(request):
    Books=Book.objects.all()
    return render(request, "bookmodule/listbooks.html",{'Books':Books})
 


def lab10_part1_addbook(request):
     if request.method=='POST':
                title=request.POST.get('title')
                price=request.POST.get('price')
                edition=request.POST.get('edition')
                author=request.POST.get('author')                
                obj = Book(title=title, price = float(price), edition = edition, author = author) 
                obj.save() 
                return redirect('books.show_one_book', id = obj.id)
            
     return render(request, "bookmodule/add_new_book.html")


def lab10_part1_editbook(request,id):
        obj = Book.objects.get(id = id)
        if request.method == 'POST':
                title=request.POST.get('title')
                price=request.POST.get('price')
                edition=request.POST.get('edition')
                author=request.POST.get('author')                
                obj.title = title
                obj.price = float(price)
                obj.edition = int(edition)
                obj.author = author
                obj.save()
                return redirect('books.show_one_book', id = obj.id)
        return render(request, "bookmodule/update_book.html", {'obj':obj})    

def lab10_part1_deletebook(request,id):
    obj = Book.objects.get(id=id)
    obj.delete()
    return redirect('books.lab10_part1_listbook') 
 
 
 
 
def lab10_part2_listbook(request):
    Books=Book.objects.all()
    return render(request, "bookmodule/listbooks2.html",{'Books':Books})
 

def lab10_part2_addbook(request):
    obj = None
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('books.show_one_book', id = obj.id)
    else: 
        form = BookForm(None)
    return render(request, "bookmodule/add_book2.html",{'form':form})


def lab10_part2_editbook(request,id):
    obj = Book.objects.get(id=id) 
    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('books.show_one_book', id=obj.id)  
    else:
            form = BookForm(instance=obj)
    return render(request, "bookmodule/update_book2.html",{'form':form})


def lab10_part2_deletebook(request,id):
    obj = Book.objects.get(id = id)
    if request.method=='POST':
         book = Book.objects.get(id=id)
         book.delete()
         return redirect('books.lab10_part2_listbook') 
    return render(request, "bookmodule/delete_book2.html", {'obj':obj})
    
 

 
def show_one_book(request,id):
    obj = Book.objects.get(id = id)
    return render(request, "bookmodule/show_one_book.html", {'obj':obj})    



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
