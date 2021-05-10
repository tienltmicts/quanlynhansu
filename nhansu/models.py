from django.db import models

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
    
class KhenThuowngKyLuat:
    class Meta:
        db_table = "khenthuong_kyluat"
        verbose_name = "KhenThuowngKyLuat"
        verbose_name_plural = "KhenThuowngKyLuat"
        
    maKTKL = models.CharField(max_length=255)
    tenKTKL = models.CharField(max_length=255)
    hinhthucKTKL = models.PositiveSmallIntegerField('Hình thức KTKL', choices=HINH_THUC_KTKL, default=0)
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
    
