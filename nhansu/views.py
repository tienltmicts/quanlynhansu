from django.shortcuts import render,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, TinhLuongForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import *
import datetime



# Create your views here.

@csrf_protect
def user_login(request):
    messages = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session.set_expiry(0)
                login(request, user)  
                return HttpResponseRedirect('/admin')
            else:
                messages = "Tên tài khoản hoặc mật khẩu của bạn không đúng"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'messages': messages})

@staff_member_required
def wage_total(request):
    nvpb = []
    nhanVienPB = NhanVienPhongBan.objects.all()
    for nv in nhanVienPB:
        nvpb.append({'id': nv.id , 'nv': str(nv)})
    if request.method == 'POST':
        form = TinhLuongForm(request.POST)
        if form.is_valid():
            nhanVien = get_object_or_404(NhanVienPhongBan, id=request.POST['nhanVien']) 
            nvKtkl = NhanVienKTKL.objects.filter(nhanVienPB=nhanVien)
            ktkl = 0
            for i in nvKtkl:
                if i.ktkl.laKT == True:
                    ktkl = ktkl  + i.ktkl.soTienKTKL
                else:
                   ktkl = ktkl  - i.ktkl.soTienKTKL 
            tong = ktkl + nhanVien.mucLuong.soTien
            phieuLuong = PhieuLuong.objects.create(
                nhanVienPB=nhanVien,
                ngayPhat=datetime.datetime.now(),
                tongTien=tong
            )
            phieuLuong.save()
            return HttpResponseRedirect('/nhansu/bangluong')        
    else:
        form = TinhLuongForm()       
    return render(request, "admin/tinhluong.html",{'form': form, 'nhanVienPB': nvpb})

def bangluong(request):
    bangLuong = []
    for i in PhieuLuong.objects.all():
        bangLuong.append(i)
    print(bangLuong)
    return render(request, "admin/bangluong.html", {'bangluong': bangLuong})  

def xoa_hangbangluong(request, id):
    pl = get_object_or_404(PhieuLuong,id=id)
    pl.delete()
    messages.success(request, 'Xoá thành công!')
    return HttpResponseRedirect('/nhansu/bangluong')
    
# def thongke_phongban(request):
#     if request.method == 'GET':
#         form = FilterTKBForm(request.GET)
#         if form.is_valid():
#             query_string=request.GET.get('paradigm')
#             if query_string == 'Học viên theo tên':
#                 students = schedule.student.all().order_by('name')
#             elif query_string == 'Học viên theo ID':
#                 students = schedule.student.all().order_by('pk')
#             else:
#                 students = schedule.student.all().order_by('birthday')
#         else:
#             form = FilterTKBForm(
#                 initial= {
#                     'paradigm': 'Học viên theo tên'
#                 }
#             )
#         return render(request, 'tkb/view_students_list.html', {
#             'students': students, 
#             'sub':sub, 
#             'id': schedule.id,
#             'filter': filters,
#             'query_string': query_string
#             })