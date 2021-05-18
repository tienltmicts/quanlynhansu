from django.urls import path


from . import views

urlpatterns = [
   path('quanly-luong/', views.quanly_luong, name="quanly_luong"),
   path('tinhluong/', views.wage_total, name="tinhluong"),
   path('bangluong/', views.bangluong, name="bangluong"),
   # path('xoahangbangluong/<int:id>/', views.xoa_hangbangluong, name="xoaHangbangluong"),
   path('thongke/', views.thongke, name="thongke"),
   path('tk-phongban/', views.thongke_phongban, name="tk_phongban"),
   path('tk-chucvu/', views.thongke_chucvu, name="tk_chucvu"),
   path('tk-luong/', views.thongke_mucluong, name="tk_luong"),
   path('tt-canhan/', views.tt_canhan, name="tt_canhan"),
   path('tt-banthan/', views.tt_banthan, name="tt_banthan"),
   path('tt-thannhan/', views.tt_thannhan, name="tt_thannhan"),
   path('tt-congtac/', views.tt_congtac, name="tt_congtac"),
   path('tt-congtac-chitiet/<int:id>/', views.tt_congtac_chitiet, name="tt_congtac_chitiet"),
   path('tt-chuyengiaophongban/', views.tt_chuyengiaopb, name="tt_chuyengiaopb"),
]
from django.contrib import admin

admin.autodiscover()