"""EIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.homepage, name='root'),
    path('search_human/', user_views.search_human, name='search_human'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('bind/', user_views.bind, name='bind'),
    path('modify/', user_views.modify, name='modify'),
    path('captcha/', include('captcha.urls')),
    path('company/', include('company.urls')),
    path('human/', include('human.urls')),
]
