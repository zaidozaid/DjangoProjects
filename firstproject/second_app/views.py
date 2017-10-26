from django.shortcuts import render
from django.http import HttpResponse

from second_app.models import user

def userr(request):
    allusers = user.objects.order_by('firstname')
    user_dict = {'all_users':allusers}
    return render(request,'second_app/users.html',context=user_dict)














