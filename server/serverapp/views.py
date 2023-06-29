import builtins
import uuid
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from server.settings import EMAIL_HOST_USER
from django.urls import reverse_lazy
from django.views import generic
# Create your views here
def signUpView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email = request.POST.get('email')
        password=request.POST.get('password')
        # proPic=request.POST.get('proPic')

        #checking whether the username exists

        if User.objects.filter(username=username).first():
            # it will get 1st object from filter query
            messages.success(request,'username is already taken')
            #message is a framework allow to store msgs in one request and retrive them in the request page

            return redirect(signUpView)

        if User.objects.filter(email=email).first():
            messages.success(request, 'email is already taken')
            return redirect(signUpView)
        user_obj=User(username=username,email=email,first_name=first_name,last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()
        #import uuid
        auth_token=str(uuid.uuid4())
        #new model is created
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        sendMailSignUp(email,auth_token)
        return render(request,'success.html')
    return render(request,'signUp.html')

def sendMailSignUp(email,auth_token):
    subject="your account has been varified"
    message=f'click the link to verify your account http://127.0.0.1:8000/inkspire/verify/{auth_token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(userLogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(userLogin)
    else:
        messages.success(request,'user not found')
        return redirect(userLogin)

def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username']=username
        user_obj= User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(userLogin)
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your email')
            return redirect(userLogin)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(userLogin)
        return redirect(index)
    return render(request,'userLogin.html')
def profileImageUpload(request):
    if request.method == 'POST':
        un = request.session['username']
        a = proImageForm(request.POST, request.FILES)
        if proImage.objects.filter(name=un).exists():
            return HttpResponse("already added")
        elif a.is_valid():
            img = a.cleaned_data['proPic']
            b=proImage(proPic=img,name=un)
            b.save()
    return render(request,'uploadprofile.html')


# def userProfile(request):
#     un=request.session['username']
#     a=proImage.objects.filter(name=un)
#     pro=[]
#     na=[]
#     for i in a:
#         z=i.name
#         na.append(z)
#         b = i.proPic
#         pro.append(str(b).split('/')[-1])
#     pi=zip(pro,na)
#     return render(request,'user_profile.html',{'username':un,'image':pi})
def landingPage(request):
    return render(request,'landingPage.html')

def index(request):
    a = blogUploadModel.objects.all()
    titleName = []
    cover = []
    sumary = []
    artistName = []
    id = []
    for i in a:
        b = i.mainTitleName
        titleName.append(b)
        c = i.image
        cover.append(str(c).split('/')[-1])
        d = i.summary
        sumary.append(d)
        e = i.blogername
        artistName.append(e)
        d = i.id
        id.append(d)
    mylist = zip(titleName, cover, sumary, artistName,id)
    un = request.session['username']
    a = proImage.objects.filter(name=un)
    pro = []
    na = []
    for i in a:
        z = i.name
        na.append(z)
        b = i.proPic
        pro.append(str(b).split('/')[-1])
    pi = zip(pro, na)
    return render(request, 'indexOne.html', {'mylist': mylist,'image':pi})
def blogUpload(request):
    if request.method=='POST':
        a=blogUploadForm(request.POST,request.FILES)
        us=request.session['username']
        if a.is_valid():
            mtn=a.cleaned_data['mainTitleName']
            img=a.cleaned_data['image']
            vid=a.cleaned_data['video']
            sum=a.cleaned_data['summary']
            stf=a.cleaned_data['subTitleNameFirst']
            pgf=a.cleaned_data['paragarphFirst']
            sts=a.cleaned_data['subTitleNameSecond']
            pgs=a.cleaned_data['paragarphSecond']
            b=blogUploadModel(blogername=us,mainTitleName=mtn,image=img,video=vid,summary=sum,subTitleNameFirst=stf,paragarphFirst=pgf,subTitleNameSecond=sts,paragarphSecond=pgs)
            b.save()
            return render(request,'up.html')
        else:
            return HttpResponse("Upload Failed")
    return render(request,"blogUpload.html")
# def blogDisplay(request,id):
#     a = blogUploadModel.objects.filter(id=id)
#     # titleName = []
#     cover = []
#     video = []
#     # sumary = []
#     # subTitleFirst = []
#     # paraFirst =[]
#     # subTitleSecond = []
#     # paraSecond = []
#     # artistName = []
#     # id = []
#     for i in a:
#         c = i.image
#         cover.append(str(c).split('/')[-1])
#         g = i.video
#         video.append(str(g).split('/')[-1])
#     mylistVideoImage = zip(cover,video)
#     return render(request,'Display.html',{'mylist':a,'my':mylistVideoImage})
# def proImage(request):
#     if request.method=='POST':
#         a=profileImageForm(request.POST,request.FILES)
#         # pp=request.session['propic']
#         if a.is_valid():
#             pp=a.cleaned_data['proPic']
#             b=profileImage(proPic=pp)
#             b.save()
#             return redirect(index)
#         else:
#             return HttpResponse("failed")
#     return render(request,'uploadprofile.html')

def singleBlogDisplayView(request,id):
    a = blogUploadModel.objects.filter(id=id)
    cover = []
    video = []
    for i in a:
        c = i.image
        cover.append(str(c).split('/')[-1])
        g = i.video
        video.append(str(g).split('/')[-1])
        h=i.blogername
    mylistVideoImage = zip(cover, video)
    x = proImage.objects.filter(name=h)
    pro = []
    na = []
    for i in x:
        z = i.name
        na.append(z)
        b = i.proPic
        pro.append(str(b).split('/')[-1])
    profile = zip(pro, na)
    return render(request,'blogDisplay.html',{'mylist':a,'my':mylistVideoImage,'profile':profile})
def userProfileView(request):
    un = request.session['username']
    a = proImage.objects.filter(name=un)
    pro = []
    na = []
    for i in a:
        z = i.name
        na.append(z)
        b = i.proPic
        pro.append(str(b).split('/')[-1])
    pi = zip(pro, na)
    return render(request,'profile.html',{'profile':pi})
class blogList(generic.ListView):
    model = blogUploadModel
    template_name = 'Display.html'
    def get(self,request):
        un = request.session['username']
        a = self.model.objects.filter(blogername=un)
        titleName = []
        cover = []
        artistName = []
        id = []
        for i in a:
            b = i.mainTitleName
            titleName.append(b)
            c = i.image
            cover.append(str(c).split('/')[-1])

            e = i.blogername
            artistName.append(e)
            d = i.id
            id.append(d)
        mylist = zip(titleName, cover, artistName, id)
        return render(request,self.template_name,{'mylist':mylist})

class deleteList(generic.ListView):
    model = blogUploadModel
    template_name = 'deletelist.html'
    def get(self,request):
        un = request.session['username']
        a = self.model.objects.filter(blogername=un)
        titleName = []
        cover = []
        artistName = []
        id = []
        for i in a:
            b = i.mainTitleName
            titleName.append(b)
            c = i.image
            cover.append(str(c).split('/')[-1])

            e = i.blogername
            artistName.append(e)
            d = i.id
            id.append(d)
        mylist = zip(titleName, cover, artistName, id)
        return render(request, self.template_name, {'mylist': mylist})

class blogDelete(generic.DeleteView):
    model = blogUploadModel
    template_name = 'conformdelete.html'
    success_url = reverse_lazy('deletelist')

