from django.conf.urls import url
from firstapp import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^formpage/',views.form_view,name='form'),
    url(r'^signup/',views.sign_up,name='signup'),
    url(r'^register/',views.register,name='register')

]
