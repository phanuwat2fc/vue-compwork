from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('member', views.MemberApi),
    re_path('member/<int:pk>', views.MemberDetail),
]