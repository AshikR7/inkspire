from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    proPic = models.FileField(upload_to='serverapp/static/profileImages')
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user

class blogUploadModel(models.Model):
    blogername=models.CharField(max_length=20)
    mainTitleName=models.CharField(max_length=40)
    image=models.ImageField(upload_to='serverapp/static/blogImages')
    video=models.FileField(upload_to='serverapp/static/blogVideo',blank=True, null=True)
    summary=models.CharField(max_length=100)
    subTitleNameFirst=models.CharField(max_length=40,blank=True, null=True)
    paragarphFirst=models.CharField(max_length=255,blank=True, null=True)
    subTitleNameSecond= models.CharField(max_length=40, blank=True, null=True)
    paragarphSecond=models.CharField(max_length=255,blank=True, null=True)

# class profileImage(models.Model):
#     proImage=models.OneToOneField(User,on_delete=models.CASCADE)
#     proPic=models.FileField(upload_to='serverapp/static/profileImages')
#     def __str__(self):
#         return self.proImage


