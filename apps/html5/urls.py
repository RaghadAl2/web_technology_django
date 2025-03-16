
from django.urls  import path
from . import views
urlpatterns = [
    path('links', views.links, name="html5.links"),
    path('text/formatting', views.formatting, name="html5.formmating"),
    path('listing', views.listing, name="html5.listing"),
    path('table', views.table, name="html5.table"),   
]
 