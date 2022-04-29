from django.db import models
from account.models import Client

# Create your models here.
class Catalogue(models.Model):
    image = models.ImageField(upload_to='pics')
    date_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_modified = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.nom

class Testimonial(models.Model):
    client = models.ForeignKey(
        Client, null=True, blank=True, on_delete=models.CASCADE, related_name="user_client"
    )
    review = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/pics', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_modified = models.DateTimeField(auto_now_add = False, auto_now = True)

    # def __str__(self):
    #     return self.nom









