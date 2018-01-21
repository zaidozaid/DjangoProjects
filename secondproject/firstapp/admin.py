from django.contrib import admin
from django.contrib import auth


from firstapp.models import MyUser
from firstapp.models import AccessRecord,Topic,Webpage,UserProfileInfo

# Register your models here.

admin.site.register(MyUser)

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)

