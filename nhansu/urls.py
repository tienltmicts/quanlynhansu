from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   path('tinhluong/', views.wage_total, name="tinhluong"),
   path('bangluong/', views.bangluong, name="bangluong"),
   path('xoahangbangluong/<int:id>/', views.xoa_hangbangluong, name="xoaHangbangluong")
]
from django.contrib import admin

admin.autodiscover()