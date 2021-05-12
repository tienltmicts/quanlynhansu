from django import forms
from django.contrib.auth.forms import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=255)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)
    
class TinhLuongForm(forms.Form):
    nhanVien = forms.Select(choices= NhanVienPhongBan.objects.all())
    
    
