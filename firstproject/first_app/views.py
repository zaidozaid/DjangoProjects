from django.shortcuts import render

# Create your views here.

def help(request):
    return render(request,"first_app/first_app.html",{'insert_me': "This is a text from views.py !"})

