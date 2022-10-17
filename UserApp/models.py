from email.policy import default
from django.db import models

# Create your models here.

class UserDB(models.Model):
    name_r = models.CharField(max_length=20)
    phone_r = models.IntegerField()
    email_r = models.CharField(max_length=20)
    pwd_r = models.CharField(max_length=20)
    status_r = models.CharField(max_length=20,default='null')
    reason_r = models.CharField(max_length=20,default='null')

class LawyerDB(models.Model):
    name_l = models.CharField(max_length=20)
    phone_l = models.IntegerField()
    enroll_l = models.IntegerField()
    law = models.CharField(max_length=20)
    email_l = models.CharField(max_length=20)
    pwd_l = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Image', default='null.jpg')
    status_l = models.CharField(max_length=20,default='null')
    reason_l = models.CharField(max_length=20,default='null')

class BookDB(models.Model):
    userid = models.ForeignKey(UserDB,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    desc = models.CharField(max_length=2000)
    status = models.CharField(max_length=20,default='null')
    room = models.CharField(max_length=20, default='null')
    reason = models.CharField(max_length=20,default='null')

class MsgDB(models.Model):
    name_m = models.CharField(max_length=20)
    email_m = models.CharField(max_length=20)
    phone_m = models.IntegerField()
    reason_m = models.CharField(max_length=100)
    message_m = models.CharField(max_length=1000)