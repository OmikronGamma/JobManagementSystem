from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('register/',registerUser,name='register'),
    path('apply/',applyPage,name='apply'),
]