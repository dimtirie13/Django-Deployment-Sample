"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from first_app import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^other/', views.other,name='other'),
    url(r'^signup',views.signup_page,name='signup'),
    url(r'^formpage/',views.form_name_view,name='form_name'),
    url(r'^relative/',views.relative,name='relative'),
    url(r'^users/', views.users,name='users'),
    url(r'^logout/$', views.user_logout,name='logout'),
    url(r'^special/', views.special,name='special'),
    url(r'^first_app/',include('first_app.urls')),
    url(r'^admin/', admin.site.urls),
]