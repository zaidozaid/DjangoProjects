from django.contrib import admin
from django.contrib import auth

# Register your models here.

from first_app.models import AccessRecord,Topic,Webpage


admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

