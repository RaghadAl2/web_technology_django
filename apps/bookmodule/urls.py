from django.urls  import path
from . import views
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('list_books/1', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search/', views.search, name="books.search"),
    path('simple/query', views.simple_query, name="books.simple_query"),
    path('complex/query', views.complex_query, name="books.complex_query"),
    path('lab8/task1/', views.lab8_task1, name="books.lab8_task1"),
    path('lab8/task2/', views.lab8_task2, name="books.lab8_task2"),
    path('lab8/task3/', views.lab8_task3, name="books.lab8_task3"),
    path('lab8/task4/', views.lab8_task4, name="books.lab8_task4"),
    path('lab8/task5/', views.lab8_task5, name="books.lab8_task5"),
     path('lab8/task7/', views.lab8_task7, name="books.lab8_task7"),
   


     
]
 
