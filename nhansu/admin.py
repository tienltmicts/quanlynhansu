from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class ChucVuAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenChucVu', 'baoHiem', 'troCap',)
    search_field = ('tenChucVu')

admin.site.register(ChucVu, ChucVuAdmin)

class MucLuongAdmin(admin.ModelAdmin):
    list_display = ('id', 'maMucLuong', 'soTien',)
    search_field = ('maMucLuong')

admin.site.register(MucLuong, MucLuongAdmin)

class PhongBanAdmin(admin.ModelAdmin):
    list_display = ('id', 'maPhongBan', 'tenPhongBan', 'diaChi',)
    search_field = ('tenPhongBan')

admin.site.register(PhongBan, PhongBanAdmin)

class KhenThuongKyLuatAdmin(admin.ModelAdmin):
    list_display = ('id', 'maKTKL', 'tenKTKL', 'hinhthucKTKL', 'soTienKTKL', 'laKT')
    search_field = ('maKTKL')

admin.site.register(KhenThuongKyLuat, KhenThuongKyLuatAdmin)

class ChuyenMonAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenChuyenMon')
    search_field = ('tenChuyenMon')

admin.site.register(ChuyenMon, ChuyenMonAdmin)

class TrinhDoNgoaiNguAdmin(admin.ModelAdmin):
    list_display = ('id', 'loaiNgonNgu')
    search_field = ('loaiNgonNgu')

admin.site.register(TrinhDoNgoaiNgu, TrinhDoNgoaiNguAdmin)

class ThanNhanAdmin(admin.ModelAdmin):
    list_display = ('id', 'hoVaTen', 'diaChi', 'soDienThoai', 'quanHe')
    search_field = ('hoVaTen')

admin.site.register(ThanNhan, ThanNhanAdmin)

class NguoiDungAdmin(admin.ModelAdmin):
    fields = ['taikhoan', 'hoVaTen', 'diaChi', 'email', 'ngaySinh', 'soDienThoai',  'thanNhan', 'trangThaiLamViec']
    list_display = ('id','taikhoan', 'hoVaTen', 'diaChi', 'email', 'ngaySinh', 'soDienThoai', 'get_hosolylich', 'get_chuyenmon','get_tdnn', 'get_thannhan', 'trangThaiLamViec' )
    search_field = ('hoVaTen', 'taikhoan')
    def get_hosolylich(self,obj):
        hoSoLyLich  = HoSoLyLich.objects.filter(nhanVien=obj)
        return mark_safe("<br/>".join([str(m) for m in hoSoLyLich]))
    get_hosolylich.short_description = 'Hồ Sơ Lý Lịch'
    
    def get_chuyenmon(self, obj):
        chuyenMon  = ChuyenMonNhanVien.objects.filter(nhanVien=obj)
        return mark_safe("<br/>".join([str(m) for m in chuyenMon]))
    get_chuyenmon.short_description = 'Chuyên Môn'
    
    def get_tdnn(self, obj):
        trinhDoNN  = TDNNNhanVien.objects.filter(nhanVien=obj)
        return mark_safe("<br/>".join([(m) for m in trinhDoNN]))
    get_tdnn.short_description = 'Trình Độ Ngoại Ngữ'
    
    def get_thannhan(self,obj):
        return obj.thanNhan
    get_thannhan.short_description = 'Thân Nhân'

admin.site.register(NguoiDung, NguoiDungAdmin)

class TDNNNhanVienAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'ngonNgu', 'mucDo')
    search_field = ('ngonNgu')

admin.site.register(TDNNNhanVien, TDNNNhanVienAdmin)

class ChuyenMonNhanVienAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'chuyenMon', 'mucDo')
    search_field = ('chuyenMon')

admin.site.register(ChuyenMonNhanVien, ChuyenMonNhanVienAdmin)

class NhanVienKTKLAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVienPB', 'ktkl', 'thoiGian')
    search_field = ('nhanVien', 'ktkl')

admin.site.register(NhanVienKTKL, NhanVienKTKLAdmin)

class PhieuLuongAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVienPB', 'ngayPhat', 'tongTien')
    search_field = ('nhanVien', 'ngayPhat')

admin.site.register(PhieuLuong, PhieuLuongAdmin)

class NhanVienPhongBanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'phongBan', 'chucVu','mucLuong','get_nvKTKL', 'get_phieuluong', 'tg_batDau', 'tg_ketThuc')
    search_field = ('nhanVien', 'phongBan')
    def get_nvKTKL(self, obj):
        nvKTKL  = NhanVienKTKL.objects.filter(nhanVienPB=obj)
        return mark_safe("<br/>".join([m for m in nvKTKL]))
    get_nvKTKL.short_description = 'Khen thưởng kỷ luật'
    
    def get_phieuluong(self, obj):
        phieuluong  = PhieuLuong.objects.filter(nhanVienPB=obj).order_by('-ngayPhat')
        return mark_safe("<br/>".join([m for m in phieuluong]))
    get_phieuluong.short_description = 'Phiếu lương'
    
admin.site.register(NhanVienPhongBan, NhanVienPhongBanAdmin)