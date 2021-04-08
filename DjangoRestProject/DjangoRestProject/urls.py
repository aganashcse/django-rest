"""DjangoRestProject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from crudapp.views import EmployeeDetails, ListEmployee, UpdateEmployee, authenticateIndex, register, ListEmployeeRest, send_email, broadcast_sms
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

# for rest_framework UI like swagger:
router = routers.DefaultRouter()
router.register('listEmployees', ListEmployeeRest)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeedetails/', EmployeeDetails),
    path('listemployees/', ListEmployee.as_view()),
    path('updateEmployee/<id>', UpdateEmployee.as_view()),
    #urls provided by django
    path('accounts/', include('django.contrib.auth.urls')),
    #urls for authentication(login, register)
    path('', authenticateIndex, name="authenticateIndex"), #for login
    path('register', register, name="register"), # for basic django user registration
    #for jwt token authentication
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/view/', TokenRefreshView.as_view()),
    #for mail(gmail)
    path('router/', include(router.urls)),
    path('sendEmail', send_email, name="send gmail"),
    #for twilio sms
    path('sendsms', broadcast_sms, name="send sms"),
]
