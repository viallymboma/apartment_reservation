from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Client(models.Model):
    client = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="user_client"
    )
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    # photo = models.ImageField(upload_to='media/pics', null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.TextField(null=True, blank=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.first_name

    # def get_full_name(self):
    #     if self.first_name is None:
    #         self.first_name = ""
    #     return f"{self.first_name} {self.last_name} {self.other_names}"









