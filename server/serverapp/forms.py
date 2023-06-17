from django import forms
# from models import UserImage
class blogUploadForm(forms.Form):
    mainTitleName = forms.CharField(max_length=40)
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    summary = forms.CharField(max_length=100)
    subTitleNameFirst = forms.CharField(max_length=40,required=False)
    paragarphFirst = forms.CharField(max_length=255,required=False)
    subTitleNameSecond = forms.CharField(max_length=40,required=False)
    paragarphSecond = forms.CharField(max_length=255,required=False)
# class profileImageForm(forms.Form):
#     proPic=forms.FileField()

# class UserProfileImageForm(forms.ModelForm):
#     class Meta:
#         model = UserImage
#
#     def clean_avatar(self):
#         avatar = self.cleaned_data['avatar']
#         return avatar

class proImageForm(forms.Form):
    proPic=forms.ImageField()