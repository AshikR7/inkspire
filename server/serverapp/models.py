from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # proPic = models.ImageField(upload_to='serverapp/static/profile_pictures/', blank=True)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

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

# class UserImage(models.Model):
#     userPic= models.OneToOneField(User,on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='serverapp/static/profileImage')

class proImage(models.Model):
    proPic = models.ImageField(upload_to='serverapp/static/profile_pictures/', blank=True)
    name=models.CharField(max_length=20)


