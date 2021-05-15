from django import forms
from django.contrib.auth.forms import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=255)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)
    
class TinhLuongForm(forms.Form):
    nhanVien = forms.Select(choices= NhanVienPhongBan.objects.all())
    
class FilterForm(forms.Form):
    param = forms.CharField(widget=forms.TextInput())
    tg_batDau = forms.DateField(widget=forms.DateInput(attrs={'class': 'vDateFfield'}))
    
class ThanNhanForm(forms.Form):   
    hoVaTen = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'vTextField'
            }), max_length=255)
    diaChi = forms.CharField(widget=forms.Textarea(
        attrs={
                'class': 'vTextField'
            }), required=False)
    soDienThoai = forms.IntegerField(required=False, widget=forms.NumberInput(
        attrs={
                'class': 'vTextField'
            }))
    quanHe = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'vTextField'
            }), max_length=255)
   