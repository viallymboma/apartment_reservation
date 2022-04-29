from django.urls import path
from .views import reservation, exit_apartment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # path("reservation/")
    path ("reservation", reservation, name= 'reservation'),
    path ("exit_apartment/", exit_apartment, name="exit_apartment")
]
urlpatterns += staticfiles_urlpatterns()
