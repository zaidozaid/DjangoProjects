from django.shortcuts import render
from django.http import HttpResponse
from firstapp import forms
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def help(request):

    my_dict ={"insert_me":"this is text from views"}

    return render(request,"firstapp/help.html",context=my_dict)


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






