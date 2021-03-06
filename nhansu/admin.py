from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.admin.views import main

class ChucVuAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenChucVu', 'baoHiem', 'troCap',)
    search_fields = ['id', 'tenChucVu']

admin.site.register(ChucVu, ChucVuAdmin)

class MucLuongAdmin(admin.ModelAdmin):
    list_display = ('id', 'maMucLuong', 'soTien',)
    search_fields = ['maMucLuong','id']

admin.site.register(MucLuong, MucLuongAdmin)

class PhongBanAdmin(admin.ModelAdmin):
    list_display = ('id', 'maPhongBan', 'tenPhongBan', 'diaChi',)
    search_fields = ['tenPhongBan','id']

admin.site.register(PhongBan, PhongBanAdmin)

class KhenThuongKyLuatAdmin(admin.ModelAdmin):
    list_display = ('id', 'maKTKL', 'tenKTKL', 'hinhthucKTKL', 'soTienKTKL', 'laKT')
    search_fields = ['maKTKL','tenKTKL','id']

admin.site.register(KhenThuongKyLuat, KhenThuongKyLuatAdmin)

class ChuyenMonAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenChuyenMon')
    search_fields = ['tenChuyenMon','id']

admin.site.register(ChuyenMon, ChuyenMonAdmin)

class TrinhDoNgoaiNguAdmin(admin.ModelAdmin):
    list_display = ('id', 'loaiNgonNgu')
    search_fields = ['loaiNgonNgu','id']

admin.site.register(TrinhDoNgoaiNgu, TrinhDoNgoaiNguAdmin)

class ThanNhanAdmin(admin.ModelAdmin):
    list_display = ('id', 'hoVaTen', 'diaChi', 'soDienThoai', 'quanHe')
    search_fields = ['hoVaTen', 'id']

admin.site.register(ThanNhan, ThanNhanAdmin)

class NguoiDungAdmin(admin.ModelAdmin):
    fields = ['taikhoan', 'hoVaTen', 'diaChi', 'email', 'ngaySinh', 'soDienThoai',  'thanNhan', 'trangThaiLamViec']
    list_display = ('id','taikhoan', 'hoVaTen', 'diaChi', 'email', 'ngaySinh', 'soDienThoai', 'get_hosolylich', 'get_chuyenmon','get_tdnn', 'get_thannhan', 'trangThaiLamViec' )
    search_fields = ['hoVaTen','id']
    def get_hosolylich(self,obj):
        hoSoLyLich  = LyLichCongTac.objects.filter(nhanVien=obj)
        return mark_safe("<br/>".join([str(m) for m in hoSoLyLich]))
    get_hosolylich.short_description = 'L?? L???ch C??ng T??c'
    
    def get_chuyenmon(self, obj):
        chuyenMon  = ChuyenMonNhanVien.objects.filter(nhanVien=obj)
        return mark_safe("<br/>".join([str(m) for m in chuyenMon]))
    get_chuyenmon.short_description = 'Chuy??n M??n'
    
    def get_tdnn(self, obj):
        trinhDoNN  = TDNNNhanVien.objects.filter(nhanVien=obj)
        return mark_safe("<br/>".join([str(m) for m in trinhDoNN]))
    get_tdnn.short_description = 'Tr??nh ????? Ngo???i Ng???'
    
    def get_thannhan(self,obj):
        return obj.thanNhan
    get_thannhan.short_description = 'Th??n Nh??n'

admin.site.register(NguoiDung, NguoiDungAdmin)

class LyLichCongTacAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'tenNoiCongTac', 'thoiGian', 'diaChi')
    search_fields = ['id','tenNoiCongTac','diaChi']

admin.site.register(LyLichCongTac, LyLichCongTacAdmin)

class TDNNNhanVienAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'ngonNgu', 'mucDo')
    search_fields = ['id','mucDo']

admin.site.register(TDNNNhanVien, TDNNNhanVienAdmin)

class ChuyenMonNhanVienAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'chuyenMon', 'mucDo')
    search_fields = ['id','mucDo']

admin.site.register(ChuyenMonNhanVien, ChuyenMonNhanVienAdmin)

class NhanVienKTKLAdmin(admin.ModelAdmin):
    list_display = ('id',  'thoiGian')
    search_fields = ['id']

admin.site.register(NhanVienKTKL, NhanVienKTKLAdmin)

# class PhieuLuongAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nhanVienPB', 'ngayPhat', 'tongTien')
#     search_field = ('nhanVien', 'ngayPhat')

# admin.site.register(PhieuLuong, PhieuLuongAdmin)

class NhanVienPhongBanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanVien', 'phongBan', 'chucVu','mucLuong','get_nvKTKL', 'get_phieuluong', 'tg_batDau', 'tg_ketThuc')
    search_fields = ['id']
    def get_nvKTKL(self, obj):
        nvKTKL  = NhanVienKTKL.objects.filter(nhanVienPB=obj)
        return mark_safe("<br/>".join([str(m) for m in nvKTKL]))
    get_nvKTKL.short_description = 'Khen th?????ng k??? lu???t'
    
    def get_phieuluong(self, obj):
        phieuluong  = PhieuLuong.objects.filter(nhanVienPB=obj).order_by('-ngayPhat')
        return mark_safe("<br/>".join([str(m) for m in phieuluong]))
    get_phieuluong.short_description = 'Phi???u l????ng'
    
admin.site.register(NhanVienPhongBan, NhanVienPhongBanAdmin)

