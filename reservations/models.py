from django.db import models
from account.models import Client
from rooms.models import Appartment

# Create your models here.
class Reservation(models.Model):
    client = models.ForeignKey(
        Client, null=True, blank=True, on_delete=models.CASCADE, related_name="user_client_bk"
    )
    appartment = models.ForeignKey(
        Appartment, null=True, blank=True, on_delete=models.CASCADE, related_name="appart_bk"
    )
    client_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(default=0, blank=True, null=True)
    date_Check_In = models.DateField(auto_now=False, blank=True, null=True)
    date_Check_Out = models.DateField(auto_now=False, blank=True, null=True)
    adult = models.IntegerField(default=0, blank=True, null=True)
    children = models.IntegerField(default=0, blank=True, null=True)
    rooms_image = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_modified = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__ (self):
        return self.client_name






