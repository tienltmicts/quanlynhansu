from django.db import models
from django.contrib.auth.models import User

# Create your models here.
HINH_THUC_KTKL = [
    (0, 'Chuyển tiền qua thẻ'),
    (1, 'Chuyển tiền mặt'),
    (2, 'Trừ lương'),
    (3, 'Thu tiền phạt'),
]

class ChucVu(models.Model):
    class Meta:
        db_table = "chucvu"
        verbose_name = "ChucVu"
        verbose_name_plural = "ChucVu"

    tenChucVu = models.CharField(max_length=255)
    baoHiem = models.CharField(max_length=255)
    troCap = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tenChucVu

class MucLuong(models.Model):
    class Meta:
        db_table = "mucluong"
        verbose_name = "MucLuong"
        verbose_name_plural = "MucLuong"

    maMucLuong = models.CharField(max_length=255)
    soTien = models.BigIntegerField()
    
    def __str__(self):
        return self.maMucLuong
    
class PhongBan(models.Model):
    class Meta:
        db_table = "phongban"
        verbose_name = "PhongBan"
        verbose_name_plural = "PhongBan"
        
    maPhongBan = models.CharField(max_length=255)
    tenPhongBan = models.CharField(max_length=255)
    diaChi =  models.CharField(max_length=255)
    
    def __str__(self):
        return self.maPhongBan
    
class KhenThuongKyLuat(models.Model):
    class Meta:
        db_table = "khenthuong_kyluat"
        verbose_name = "KhenThuongKyLuat"
        verbose_name_plural = "KhenThuongKyLuat"
        
    maKTKL = models.CharField(max_length=255)
    tenKTKL = models.CharField(max_length=255)
    hinhthucKTKL = models.PositiveSmallIntegerField( choices=HINH_THUC_KTKL, default=0)
    soTienKTKL = models.BigIntegerField(null= True, blank=True)
    laKT = models.BooleanField("Đây là Khen thưởng", default=True)
    
    def __str__(self):
        return self.maKTKL
    
class ChuyenMon(models.Model):
    class Meta:
        db_table = "chuyenmon"
        verbose_name = "ChuyenMon"
        verbose_name_plural = "ChuyenMon"
        
    tenChuyenMon = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tenChuyenMon
    
class TrinhDoNgoaiNgu(models.Model):
    class Meta:
        db_table = "trinhdoNN"
        verbose_name = "TrinhDoNgoaiNgu"
        verbose_name_plural = "TrinhDoNgoaiNgu"
        
    loaiNgonNgu = models.CharField(max_length=255)
    
    def __str__(self):
        return self.loaiNgonNgu
    
class ThanNhan(models.Model):
    class Meta:
        db_table = "thannhan"
        verbose_name = "ThanNhan"
        verbose_name_plural = "ThanNhan"
        
    hoVaTen = models.CharField(max_length=255)
    diaChi = models.TextField()
    soDienThoai = models.BigIntegerField(null= True, blank=True)
    quanHe = models.CharField(max_length=255)
    
    def __str__(self):
        return self.hoVaTen
    
class NguoiDung(models.Model):
    class Meta:
        db_table = "nguoidung"
        verbose_name = "NguoiDung"
        verbose_name_plural = "NguoiDung"
    taikhoan = models.OneToOneField(User, on_delete=models.CASCADE)    
    hoVaTen = models.CharField(max_length=255)
    diaChi = models.TextField()
    email = models.CharField(max_length=255)
    ngaySinh = models.DateField(null=True, blank=True)
    soDienThoai = models.BigIntegerField(null= True, blank=True)
    thanNhan = models.ForeignKey(ThanNhan, on_delete=models.CASCADE, blank=True, null=True)
    trangThaiLamViec = models.BooleanField("Đang làm việc", default=True)
    def __str__(self):
        return self.hoVaTen
    
class LyLichCongTac(models.Model):
    class Meta:
        db_table = "lyLichCongTac"
        verbose_name = "LyLichCongTac"
        verbose_name_plural = "LyLichCongTac"
        
    nhanVien = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    tenNoiCongTac = models.CharField(max_length=255)
    thoiGian = models.CharField(max_length=255)
    diaChi = models.TextField()
    
class TDNNNhanVien(models.Model):
    class Meta:
        db_table = "tdnn_nhanvien"
        verbose_name = "TDNNNhanVien"
        verbose_name_plural = "TDNNNhanVien"
    
    nhanVien = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    ngonNgu = models.ForeignKey(TrinhDoNgoaiNgu, on_delete=models.CASCADE)
    mucDo = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.ngonNgu)+"-"+ str(self.mucDo)
    
    
class ChuyenMonNhanVien(models.Model):
    
    class Meta:
        db_table = "chuyenmon_nhanvien"
        verbose_name = "ChuyenMonNhanVien"
        verbose_name_plural = "ChuyenMonNhanVien"
        
    nhanVien = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    chuyenMon = models.ForeignKey(ChuyenMon, on_delete=models.CASCADE)
    mucDo = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.chuyenMon)+"-"+ str(self.mucDo)

class NhanVienPhongBan(models.Model):
    class Meta:
        db_table = "nhanvien_phongban"
        verbose_name = "NhanVienPhongBan"
        verbose_name_plural = "NhanVienPhongBan"
        
    nhanVien = models.ForeignKey(NguoiDung, on_delete=models.CASCADE, blank=True, null=True)
    phongBan = models.ForeignKey(PhongBan, on_delete=models.CASCADE, blank=True, null=True)
    chucVu = models.ForeignKey(ChucVu, on_delete=models.CASCADE, blank=True, null=True)
    mucLuong = models.ForeignKey(MucLuong, on_delete=models.CASCADE, blank=True, null=True)
    tg_batDau = models.DateField("Thời gian bắt đầu", null=True, blank=True)
    tg_ketThuc = models.DateField("Thời gian kết thúc",null=True, blank=True)
    
    def __str__(self):
        return str(self.phongBan)+ "-"+ str(self.nhanVien)
    
class NhanVienKTKL(models.Model):
    class Meta:
        db_table = "nhanVienKTKL"
        verbose_name = "NhanVienKTKL"
        verbose_name_plural = "NhanVienKTKL"
        
    nhanVienPB = models.ForeignKey(NhanVienPhongBan, on_delete=models.CASCADE,blank=True, null=True)
    ktkl = models.ForeignKey(KhenThuongKyLuat, on_delete=models.CASCADE)
    thoiGian = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.ktkl)+"-"+ str(self.thoiGian)
    
class PhieuLuong(models.Model):
    class Meta:
        db_table = "phieuluong"
        verbose_name = "PhieuLuong"
        verbose_name_plural = "PhieuLuong"
        
    nhanVienPB = models.ForeignKey(NhanVienPhongBan, on_delete=models.CASCADE)
    ngayPhat = models.DateField(null=True, blank=True)
    tongTien = models.BigIntegerField()