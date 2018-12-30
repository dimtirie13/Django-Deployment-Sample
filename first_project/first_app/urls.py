from django.conf.urls import url
from first_app import views

# for template tagging
app_name = 'first_app'


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^other',views.other,name='other'),
    url(r'^signup',views.signup_page,name='signup'),
    url(r'^$', views.users,name='users'),
    url(r'^$',views.form_name_view,name='form_name'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^user_login/', views.user_login,name='user_login'),


]