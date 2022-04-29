from django.urls import path
from .views import index,contact,blog,about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',index, name= 'index'),
    path ("Contact",contact,name= 'contact'),
    path ("Blog",blog,name= 'blog'),
    path ("About",about,name= 'about'),    
]
urlpatterns += staticfiles_urlpatterns()
