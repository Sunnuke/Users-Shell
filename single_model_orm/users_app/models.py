from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CarField(max_length=45)
    last_name = models.CarField(max_length=45)
    email_address = models.CarField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)