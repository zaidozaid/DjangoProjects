from django.shortcuts import render
from django.http import HttpResponse
from firstapp import forms
# Create your views here.

def index(request):
    return render(request, "index.html",)



def form_view(request):

    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Sucess")
            print("Name:"+form.cleaned_data["name"])
            print("Email:"+form.cleaned_data["email"])
            print("Text:"+form.cleaned_data["textarea"])





    return render(request,"formpage.html",{'form':form})

def sign_up(request):
    form = forms.SignUp()

    if request.method == "POST":
        form = forms.SignUp(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request, "signup.html", {'form': form})




def register(request):
    restration = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfor(data=request.POST)
        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            

