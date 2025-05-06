from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .models import Address,Address2
from .models import Student,Student2,Image
from django.db.models import Q, Count, Min, Max, Sum, Avg
from .forms import BookForm,StudentForm,Student2Form,ImageForm
from django.contrib.auth.decorators import login_required




@login_required(login_url='/users/login')
def index(request):
    Books=Book.objects.all()
    return render(request, "bookmodule/listbooks.html",{'Books':Books})
@login_required(login_url='/users/login')
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})
@login_required(login_url='/users/login')
def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
@login_required(login_url='/users/login')  
def lab8_task1(request):
    mybooks=Book.objects.filter(Q(price__lte=80))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'All the Prices are higher than 80'})  
@login_required(login_url='/users/login')       
def lab8_task2(request):
    mybooks=Book.objects.filter(Q(edition__gte=3)&(Q(title__icontains="co")|Q(author__icontains="co")))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'There is no elements to display'})  
    
@login_required(login_url='/users/login')          
def lab8_task3(request):
    mybooks=Book.objects.filter(~Q(edition__gte=2)&(~Q(title__icontains="ll")|~Q(author__icontains="co")))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'There is no elements to display'})  
     
@login_required(login_url='/users/login')          
def lab8_task4(request):
    mybooks=Book.objects.all().order_by('title')
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html',{'message':'There is no elements to display'})  
      
@login_required(login_url='/users/login')  
          
def lab8_task5(request):
    query = Book.objects.aggregate(
    count=Count('id'),
    total=Sum('price', default=0),
    average=Avg('price',default=0),
    max=Max('price',default=0) ,
    min=Min('price',default=0) ,
    )

    return render(request, 'bookmodule/books_info.html',{'query':query})


@login_required(login_url='/users/login')  

def lab8_task7(request):
    query = Student.objects.values('address__city').annotate(total=Count('id'))
    return render(request, 'bookmodule/Student_list.html',{'query':query})

@login_required(login_url='/users/login')  
def lab10_part1_listbook(request):
    Books=Book.objects.all()
    return render(request, "bookmodule/listbooks.html",{'Books':Books})
 

@login_required(login_url='/users/login')
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

@login_required(login_url='/users/login')
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
@login_required(login_url='/users/login')
def lab10_part1_deletebook(request,id):
    obj = Book.objects.get(id=id)
    obj.delete()
    return redirect('books.lab10_part1_listbook') 
 
 
 
@login_required(login_url='/users/login')
def lab10_part2_listbook(request):
    Books=Book.objects.all()
    return render(request, "bookmodule/listbooks2.html",{'Books':Books})
 
@login_required(login_url='/users/login')
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

@login_required(login_url='/users/login')
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

@login_required(login_url='/users/login')
def lab10_part2_deletebook(request,id):
    obj = Book.objects.get(id = id)
    if request.method=='POST':
         book = Book.objects.get(id=id)
         book.delete()
         return redirect('books.lab10_part2_listbook') 
    return render(request, "bookmodule/delete_book2.html", {'obj':obj})

@login_required(login_url='/users/login') 
def show_one_book(request,id):
    obj = Book.objects.get(id = id)
    return render(request, "bookmodule/show_one_book.html", {'obj':obj})    

####################################################################################################################################################################################
@login_required(login_url='/users/login')
def lab11_task1_liststudent(request):
    Students=Student.objects.all()
    return render(request, "bookmodule/lab11_task1/liststudent.html",{'Students':Students})


@login_required(login_url='/users/login')
def lab11_task1_addstudent(request):
    obj = None
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('books.lab11_task1_liststudent')
    else: 
        form = StudentForm(None)
    return render(request, "bookmodule/lab11_task1/add_student.html",{'form':form})

@login_required(login_url='/users/login')
def lab11_task1_editstudent(request,id):
    obj = Student.objects.get(id=id) 
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('books.lab11_task1_liststudent')
    else:
            form = StudentForm(instance=obj)
    return render(request, "bookmodule/lab11_task1/edit_student.html",{'form':form})

@login_required(login_url='/users/login')
def lab11_task1_deletestudent(request,id):
    obj = Student.objects.get(id = id)
    if request.method=='POST':
         student = Student.objects.get(id=id)
         student.delete()
         return redirect('books.lab11_task1_liststudent') 
    return render(request, "bookmodule/lab11_task1/delete_student.html", {'obj':obj})







@login_required(login_url='/users/login')
def lab11_task2_liststudent(request):
    Students=Student2.objects.all()
    return render(request, "bookmodule/lab11_task2/liststudent.html",{'Students':Students})

@login_required(login_url='/users/login')
def lab11_task2_addstudent(request):
    obj = None
    if request.method=='POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('books.lab11_task2_liststudent')
    else: 
        form = Student2Form(None)
    return render(request, "bookmodule/lab11_task2/add_student.html",{'form':form})

@login_required(login_url='/users/login')
def lab11_task2_editstudent(request,id):
    obj = Student2.objects.get(id=id) 
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('books.lab11_task2_liststudent')
    else:
            form = Student2Form(instance=obj)
    return render(request, "bookmodule/lab11_task2/edit_student.html",{'form':form})

@login_required(login_url='/users/login')
def lab11_task2_deletestudent(request,id):
    obj = Student2.objects.get(id = id)
    if request.method=='POST':
         student = Student2.objects.get(id=id)
         student.delete()
         return redirect('books.lab11_task2_liststudent') 
    return render(request, "bookmodule/lab11_task2/delete_student.html", {'obj':obj})

@login_required(login_url='/users/login')
def lab11_task3_listimages(request):
    Images=Image.objects.all()
    return render(request,"bookmodule/lab11task3/list.html",{"Images":Images})
@login_required(login_url='/users/login')
def lab11_task3_addimage(request):
    if request.method == 'POST':
       form = ImageForm(request.POST, request.FILES)
       if form.is_valid():
            form.save()
            return redirect('books.lab11_task3_listimages') 

    else:
        form = ImageForm()
    return render(request, 'bookmodule/lab11task3/addimage.html', {'form': form})



##########################################################################################
@login_required(login_url='/users/login')
def list_books(request):
    return render(request, 'bookmodule/list_books.html')

@login_required(login_url='/users/login')
def viewbook(request):
    return render(request, 'bookmodule/one_book.html')


@login_required(login_url='//users/login')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

@login_required(login_url='/users/login')
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

