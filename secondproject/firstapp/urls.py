from django.conf.urls import url
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^formpage/',views.form_view,name='form'),
    url(r'^signup/',views.sign_up,name='signup'),
    url(r'^register/',views.register,name='register'),
    url(r'^register/',views.register,name='register'),
    url(r'^user_login/',views.user_login,name='user_login'),

]
