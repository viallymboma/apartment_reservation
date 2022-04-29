from django.contrib import admin
from .models import Appartment

# Register your models here.
class AppartmentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name", 
        "code", 
        "price", 
        "description", 
        "image", 
        "availability", 
        "date_added", 
        "date_modified"
    ]

    class Meta:
        model = Appartment

admin.site.register(Appartment, AppartmentAdmin)