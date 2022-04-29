from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("allRooms",views.allRooms, name= 'allRooms'),
    path("api/get_all_rooms/", views.get_all_rooms, name='get_all_rooms'),
    path("api/get_a_room/", views.get_a_room, name='get_a_rooms')
    
]

urlpatterns += staticfiles_urlpatterns()
