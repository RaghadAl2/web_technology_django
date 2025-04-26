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
    path('lab10_part1/listbook/', views.lab10_part1_listbook, name="books.lab10_part1_listbook"),
    path('lab10_part1/addbook/', views.lab10_part1_addbook, name="books.lab10_part1_addbook"),
    path('lab10_part1/editbook/<id>', views.lab10_part1_editbook, name="books.lab10_part1_editbook"),
    path('lab10_part1/deletebook/<id>', views.lab10_part1_deletebook, name="books.lab10_part1_deletebook"),
    path('show_one_book/<id>', views.show_one_book, name="books.show_one_book"),
     path('lab10_part2/listbook/', views.lab10_part2_listbook, name="books.lab10_part2_listbook"),
    path('lab10_part2/addbook/', views.lab10_part2_addbook, name="books.lab10_part2_addbook"),
    path('lab10_part2/editbook/<id>', views.lab10_part2_editbook, name="books.lab10_part2_editbook"),
     path('lab10_part2/deletebook/<id>', views.lab10_part2_deletebook, name="books.lab10_part2_deletebook"),

  
]
 
