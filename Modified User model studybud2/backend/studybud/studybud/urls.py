# this urls .py is going to be for the entire project
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),    #so when every url matches empty string, it will go to the base.urls file . this will take us to the home page. and let base.urls handle the rest of the routing...this file is present in the base folder and it is the urls.py file that we are taretting
    
    path('api/',include('base.api.urls')),
]

# so we are setting the url and the file path is gonna be "MEDIA_URL" from settings  ..and we are telling it set the url and get the file from "MEDIA_ROOT"
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)