"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include

from django.contrib import admin
from django.urls import path
from myfirstapp import views
from myfirstapp.models import complaint_register


urlpatterns = [
    path('admin/', admin.site.urls),
   # path("views.index,name="homepage),
    path('demo/',views.concate,name="UpperCaseConacatenationPage"),
    path('com/',views.com,name="Page"),
    path('userview/',views.userviewcomplaint,name="View"),
    path('superlogin/',views.superuserlogin,name="SuperUserLogin"),
    url(r'^update/(?P<Id>\d+)/$',views.update, name='deletemeview'), 
]
