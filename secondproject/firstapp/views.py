from django.shortcuts import render
from firstapp import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


def user_login(request):

    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"),password=request.POST.get("password"))

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse("Account Not Active!")

        else:
            print("Some one tried to login & failed")
            return HttpResponse("Invaild Login Details")
    else:
        return render(request, "login.html",{})








@login_required()
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))



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
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfor(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:

        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfor()


    return render(request, "registration.html", {'user_form':user_form,'profile_form':profile_form,'registered':registered})




