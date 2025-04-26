
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',include("apps.bookmodule.urls")),
    path('students/',include("apps.studentmodule.urls")),
    path('users/',include("apps.usermodule.urls")),
    path('html5/',include("apps.html5.urls"))

    
]

