from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   path('tinhluong/', views.wage_total, name="tinhluong"),
   path('bangluong/', views.bangluong, name="bangluong"),
   path('xoahangbangluong/<int:id>/', views.xoa_hangbangluong, name="xoaHangbangluong"),
   path('tk-phongban/', views.thongke_phongban, name="tk_phongban"),
   path('tk-chucvu/', views.thongke_chucvu, name="tk_chucvu"),
   path('tk-luong/', views.thongke_mucluong, name="tk_luong")
]
from django.contrib import admin

admin.autodiscover()