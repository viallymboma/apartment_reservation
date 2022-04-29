from django.urls import path
from .views import login_view, logout, register, room_management, add_rooms, client_dashboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # Authentications
    path ("Register", register, name= 'register'),
    path ("Login", login_view, name= 'login'),
    path('', logout, name="logout"),

    # Accounts
    path ("Admin_dashboard", room_management, name= 'admin_dasboard'),
    path ("Admin_add_rooms", add_rooms, name= 'add_rooms'),

    path ("my_dasboard", client_dashboard, name='client_dashboard'),

]
urlpatterns += staticfiles_urlpatterns()
