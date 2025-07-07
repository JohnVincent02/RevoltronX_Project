from django.db import models
from Guest.models import *

class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_gender=models.CharField(max_length=30)
    user_dob=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)


# Create your models here.
