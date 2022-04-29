from django.db import models

# Create your models here.
class Appartment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/pics', blank=True, null=True)
    availability = models.BooleanField(blank=True, null=True, default=True)

    date_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_modified = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.name





