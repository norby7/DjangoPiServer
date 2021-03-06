"""DjangoPiServer URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.urls import views as auth
from django.views.generic.base import TemplateView # new
from authentication import views as auth_view

urlpatterns = [
    path('test_user/', auth_view.testUser,name='test_user'),
    path('', auth_views.LoginView.as_view()),
    path('login_user/', auth_view.loginUser, name='login_user'),
    path('reset_password/', auth_view.sentPasswordReset, name='reset_password'),
    path('create_user/', auth_view.createUser, name='create_user'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('reminder/home/', TemplateView.as_view(template_name='reminder/home.html'), name='reminder_home'),
]
