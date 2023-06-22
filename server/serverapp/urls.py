from django.urls import path
from .views import *
urlpatterns=[
    path('landing/',landingPage),
    path('signup/',signUpView),
    path('verify/<auth_token>',verify),
    path('login/',userLogin),
    path('index/',index),
    path('blogupload/',blogUpload),
    # path('blogdisplay/<int:id>',blogDisplay),
    path('proimageupload',profileImageUpload),
    path('singleblogdisplay/<int:id>',singleBlogDisplayView),
    path('userprofile/',userProfileView),
    path('cards',card)


]