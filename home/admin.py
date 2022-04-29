from django.contrib import admin
from .models import Catalogue, Testimonial
# Register your models here.

from .models import Client

# Register your models here.
class CatalogueAdmin(admin.ModelAdmin):
    list_display = [
        "image", 
        "date_added", 
        "date_modified"
    ]

    class Meta:
        model = Catalogue

class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        "client", 
        "review", 
        "image", 
        "date_added", 
        "date_modified"
    ]

    class Meta:
        model = Testimonial

admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Testimonial, TestimonialAdmin)



