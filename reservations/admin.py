from django.contrib import admin
from .models import Reservation

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "client", 
        "appartment", 
        "client_name", 
        "phone", 
        "date_Check_In", 
        "date_Check_Out", 
        "adult", 
        "children", 
        "rooms_image", 
        "comment", 
        "date_added", 
        "date_modified", 
    ]

    class Meta:
        model = Reservation

admin.site.register(Reservation, ReservationAdmin)
