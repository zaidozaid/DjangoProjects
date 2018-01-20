from django import forms
from firstapp.models import MyUser,UserProfileInfo
from django.contrib.auth.forms import User



class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    textarea = forms.CharField(widget=forms.Textarea)



class SignUp(forms.ModelForm):


    class Meta():
        model = MyUser
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class meta():
        model = User
        fields = ('username','email','password')



class UserProfileInfor(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','picture')















