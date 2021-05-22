from django.shortcuts import render,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, TinhLuongForm, FilterForm,ThanNhanForm
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

def quanly_luong(request):
    return render(request, 'admin/quanly_luong.html')

@staff_member_required
def wage_total(request):
    nvpb = []
    nhanVienPB = NhanVienPhongBan.objects.all()
    messages = ''
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
            messages = 'Bạn đã tính lương thành công!'       
    else:
        form = TinhLuongForm()       
    return render(request, "admin/tinhluong.html",{'form': form, 'nhanVienPB': nvpb, 'messages': messages})

def bangluong(request):
    bangLuong = []
    for i in PhieuLuong.objects.all():
        bangLuong.append(i)
    return render(request, "admin/bangluong.html", {'bangluong': bangLuong})  

# def xoa_hangbangluong(request, id):
#     pl = get_object_or_404(PhieuLuong,id=id)
#     pl.delete()
#     messages.success(request, 'Xoá thành công!')
#     return HttpResponseRedirect('/nhansu/bangluong')
    
def thongke(request):
    return  render(request, 'admin/thongke.html')
    
def thongke_phongban(request):
    nvpb = []
    phongBan = PhongBan.objects.all()
    filters = []
    query_string = 0
    nhanVien=''
    tg_batDau = ''
    tg_ketThuc = ''
    messages = ''
    for pb in phongBan:
        filters.append(pb.tenPhongBan)
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            query_string=request.GET['param']
            tg_batDau = request.GET['tg_batDau']
            tg_ketThuc = request.GET['tg_ketThuc']
            pB = get_object_or_404(PhongBan,tenPhongBan=query_string)
            nhanVien = NhanVienPhongBan.objects.filter(phongBan=pB,tg_batDau__gt=tg_batDau, tg_ketThuc__lt=tg_ketThuc).order_by('tg_batDau')
            for nv in nhanVien:
                nvpb.append(nv)
            if nvpb == []:
                messages = 'Không có nhân viên nào ở phòng ban này trong khoảng thời gian trên!'
    else:
        form = FilterForm()

    return render(request, 'admin/tk_phongban.html', {
        'form': form,
        'filter': filters,
        'query_string': query_string,
        'nhanVien': nvpb,
        'messages': messages
        })
    
def thongke_chucvu(request):
    nvpb = []
    chucVu = ChucVu.objects.all()
    filters = []
    query_string = ''
    nhanVien = ''
    tg_batDau = ''
    tg_ketThuc = ''
    messages = ''
    for cv in chucVu:
        filters.append(cv.tenChucVu)
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            query_string = request.GET['param']
            tg_batDau = request.GET['tg_batDau']
            tg_ketThuc = request.GET['tg_ketThuc']
            
            cV = get_object_or_404(ChucVu,tenChucVu=query_string)
            nhanVien = NhanVienPhongBan.objects.filter(chucVu=cV,tg_batDau__lt=tg_batDau, tg_ketThuc__gt=tg_ketThuc).order_by('tg_batDau')
            for nv in nhanVien:
                nvpb.append(nv)
            if nvpb == []:
                messages = 'Không có nhân viên nào làm chức vụ này trong khoảng thời gian trên!'
    else:
        form = FilterForm()

    return render(request, 'admin/tk_chucvu.html', {
        'form': form,
        'filter': filters,
        'query_string': query_string,
        'nhanVien': nvpb,
        'tg_batDau': tg_batDau,
        'tg_ketThuc': tg_ketThuc,
        'messages': messages
        })
    
def thongke_mucluong(request):
    nvpb = []
    filters = ['Dưới 5 triệu', 'Từ 5-10 triệu', 'Từ 10-15 triệu', 'Từ 15-20 triệu', 'Từ 20-30 triệu', 'Trên 30 triệu']
    query_string = ''
    nhanVien=''
    mucLuong = ''
    messages = ''
    tg_batDau = ''
    tg_ketThuc = ''
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            query_string=request.GET['param']
            tg_batDau = request.GET['tg_batDau']
            tg_ketThuc = request.GET['tg_ketThuc']
            if query_string == 'Dưới 5 triệu':
                mucLuong = MucLuong.objects.filter(soTien__lt=5000000).order_by('-soTien')
            elif query_string == 'Từ 5-10 triệu':
                mucLuong = MucLuong.objects.filter(soTien__gt=5000000, soTien__lt=1000000).order_by('-soTien')
            elif query_string == 'Từ 10-15 triệu':
                mucLuong = MucLuong.objects.filter(soTien__gt=9999999, soTien__lt=15000000).order_by('-soTien')
            elif query_string == 'Từ 15-20 triệu':
                mucLuong = MucLuong.objects.filter(soTien__gt=14999999, soTien__lt=20000000).order_by('-soTien') 
            elif query_string == 'Từ 20-30 triệu':
                mucLuong = MucLuong.objects.filter(soTien__gt=19000000, soTien__lt=30000000).order_by('-soTien')
            else: 
                mucLuong = MucLuong.objects.filter(soTien__gt=30000000).order_by('-soTien')
               
            for ml in mucLuong:
                nhanVien = NhanVienPhongBan.objects.filter(mucLuong=ml,tg_batDau__lt=tg_batDau, tg_ketThuc__gt=tg_ketThuc).order_by('tg_batDau')
                for nv in nhanVien:
                    nvpb.append(nv)
            if nvpb == []:
                messages = 'Không có nhân viên nào có mức lương trong khoảng này!'
    else:
        form = FilterForm()

    return render(request, 'admin/tk_mucluong.html', {
        'form': form,
        'filter': filters,
        'query_string': query_string,
        'nhanVien': nvpb,
        'messages': messages
        })

def tt_canhan(request):
    return render(request, "admin/tt_canhan.html")

def tt_banthan(request):
    nguoiDung = get_object_or_404(NguoiDung,taikhoan=request.user)
    cmon = ChuyenMonNhanVien.objects.filter(nhanVien=nguoiDung)
    tdnn = TDNNNhanVien.objects.filter(nhanVien=nguoiDung)
    chuyenMon = ''.join(str(cm) for cm in cmon)
    trinhDoNN = ''.join(str(t) for t in tdnn)
     
    return render(request, 'admin/tt_banthan.html', {'nguoiDung': nguoiDung, 'chuyenMon': chuyenMon, 'trinDoNN': trinhDoNN})


def tt_thannhan(request):
    nguoiDung = get_object_or_404(NguoiDung,taikhoan=request.user)
    thanNhan = nguoiDung.thanNhan 
    messages = ''
    if request.method == 'POST':
        
        form = ThanNhanForm(request.POST)
        if form.is_valid():
            hoVaTen = request.POST['hoVaTen']
            diaChi = request.POST['diaChi']
            soDienThoai = request.POST['soDienThoai']
            quanHe = request.POST['quanHe']
            print(quanHe)
            if hoVaTen != thanNhan.hoVaTen:
                thanNhan.delete()
                tn = ThanNhan.objects.create(
                    hoVaTen = hoVaTen,
                    diaChi = diaChi,
                    soDienThoai = soDienThoai,
                    quanHe = quanHe
                )
                tn.save()
                thanNhan = tn
            else: 
                ThanNhan.objects.filter(id=thanNhan.id).update(
                    hoVaTen = hoVaTen,
                    diaChi = diaChi,
                    soDienThoai = soDienThoai,
                    quanHe = quanHe
                ) 
            messages = 'Bạn đã sửa thông tin thành công!'
                         
    else:
        form = ThanNhanForm( 
            initial={
                'hoVaTen': thanNhan.hoVaTen,
                'diaChi': thanNhan.diaChi,
                'soDienThoai': thanNhan.soDienThoai,
                'quanHe': thanNhan.quanHe
                    
            })
    return render(request, 'admin/tt_thannhan.html', {'form':form, 'nguoiDung': nguoiDung, 'messages': messages})

def tt_congtac(request):
    nguoiDung = get_object_or_404(NguoiDung,taikhoan=request.user)
    ctac = LyLichCongTac.objects.filter(nhanVien=nguoiDung)
    congTac = []
    for ct in ctac:
        congTac.append(ct)
     
    return render(request, 'admin/tt_congtac.html', {'nguoiDung': nguoiDung, 'congTac': congTac})

def tt_congtac_chitiet(request,id):
    congTac = get_object_or_404(LyLichCongTac,id=id)  
    return render(request, 'admin/tt_congtac_chitiet.html', {'congTac': congTac})

def tt_chuyengiaopb(request):
    nguoiDung = get_object_or_404(NguoiDung,taikhoan=request.user)
    phongBan = NhanVienPhongBan.objects.filter(nhanVien=nguoiDung).order_by('tg_batDau')
      
    return render(request, 'admin/tt_chuyengiaopb.html', {'nguoiDung': nguoiDung,'phongBan': phongBan })