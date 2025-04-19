from django.urls  import path
from . import views
urlpatterns = [
    path('lab9/task1/', views.lab9_task1, name="books.lab9_task1"),
    path('lab9/task2/', views.lab9_task2, name="books.lab9_task2"),
    path('lab9/task3/', views.lab9_task3, name="books.lab9_task3"),
    path('lab9/task4/', views.lab9_task4, name="books.lab9_task4"),

]
 
