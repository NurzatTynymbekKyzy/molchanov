
from django.contrib import admin
from django.urls import path,include
from blog.views import *

urlpatterns = [
    path('',redirect_blog),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    
]
