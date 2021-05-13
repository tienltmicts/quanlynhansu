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
        verbose_name = "Chức Vụ"
        verbose_name_plural = "Chức vụ"

    tenChucVu = models.CharField(max_length=255)
    baoHiem = models.CharField(max_length=255)
    troCap = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tenChucVu

class MucLuong(models.Model):
    class Meta:
        db_table = "mucluong"
        verbose_name = "Mức Lương"
        verbose_name_plural = "Mức Lương"

    maMucLuong = models.CharField(max_length=255)
    soTien = models.BigIntegerField()
    
    def __str__(self):
        return self.maMucLuong
    
class PhongBan(models.Model):
    class Meta:
        db_table = "phongban"
        verbose_name = "Phòng Ban"
        verbose_name_plural = "Phòng Ban"
        
    maPhongBan = models.CharField(max_length=255)
    tenPhongBan = models.CharField(max_length=255)
    diaChi =  models.CharField(max_length=255)
    
    def __str__(self):
        return self.maPhongBan
    
class KhenThuongKyLuat(models.Model):
    class Meta:
        db_table = "khenthuong_kyluat"
        verbose_name = "Khen Thưởng Kỷ Luật"
        verbose_name_plural = "Khen Thưởng Kỷ Luật"
        
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
        verbose_name = "Chuyên Môn"
        verbose_name_plural = "Chuyên Môn"
        
    tenChuyenMon = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tenChuyenMon
    
class TrinhDoNgoaiNgu(models.Model):
    class Meta:
        db_table = "trinhdoNN"
        verbose_name = "Trình Độ Ngoại Ngữ"
        verbose_name_plural = "Trình Độ Ngoại Ngữ"
        
    loaiNgonNgu = models.CharField(max_length=255)
    
    def __str__(self):
        return self.loaiNgonNgu
    
class ThanNhan(models.Model):
    class Meta:
        db_table = "thannhan"
        verbose_name = "Thân Nhân"
        verbose_name_plural = "Thân Nhân"
        
    hoVaTen = models.CharField(max_length=255)
    diaChi = models.TextField()
    soDienThoai = models.BigIntegerField(null= True, blank=True)
    quanHe = models.CharField(max_length=255)
    
    def __str__(self):
        return self.hoVaTen
    
class NguoiDung(models.Model):
    class Meta:
        db_table = "nguoidung"
        verbose_name = "Người Dùng"
        verbose_name_plural = "Người Dùng"
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
        verbose_name = "Lý Lịch Công Tác"
        verbose_name_plural = "Lý Lịch công Tác"
        
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
        verbose_name = "Phiếu Lương"
        verbose_name_plural = "Phiếu Lương"
        
    nhanVienPB = models.ForeignKey(NhanVienPhongBan, on_delete=models.CASCADE)
    ngayPhat = models.DateField(null=True, blank=True)
    tongTien = models.BigIntegerField()
    