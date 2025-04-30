
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',include("apps.bookmodule.urls")),
    path('students/',include("apps.studentmodule.urls")),
    path('users/',include("apps.usermodule.urls")),
    path('html5/',include("apps.html5.urls"))


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
