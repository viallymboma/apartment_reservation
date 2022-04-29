from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "first_name", 
        "last_name", 
        "date_of_birth", 
        # "photo", 
        "email", 
        "address", 
        "city", 
        "phone", 
        "date_added", 
        "date_modified"
    ]

    class Meta:
        model = Client

admin.site.register(Client, ClientAdmin)