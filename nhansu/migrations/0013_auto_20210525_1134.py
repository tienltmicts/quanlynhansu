# Generated by Django 3.2.2 on 2021-05-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhansu', '0012_auto_20210512_0905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chucvu',
            options={'verbose_name': 'Chức Vụ', 'verbose_name_plural': 'Chức vụ'},
        ),
        migrations.AlterModelOptions(
            name='chuyenmon',
            options={'verbose_name': 'Chuyên Môn', 'verbose_name_plural': 'Chuyên Môn'},
        ),
        migrations.AlterModelOptions(
            name='khenthuongkyluat',
            options={'verbose_name': 'Khen Thưởng Kỷ Luật', 'verbose_name_plural': 'Khen Thưởng Kỷ Luật'},
        ),
        migrations.AlterModelOptions(
            name='lylichcongtac',
            options={'verbose_name': 'Lý Lịch Công Tác', 'verbose_name_plural': 'Lý Lịch công Tác'},
        ),
        migrations.AlterModelOptions(
            name='mucluong',
            options={'verbose_name': 'Mức Lương', 'verbose_name_plural': 'Mức Lương'},
        ),
        migrations.AlterModelOptions(
            name='nguoidung',
            options={'verbose_name': 'Người Dùng', 'verbose_name_plural': 'Người Dùng'},
        ),
        migrations.AlterModelOptions(
            name='phieuluong',
            options={'verbose_name': 'Phiếu Lương', 'verbose_name_plural': 'Phiếu Lương'},
        ),
        migrations.AlterModelOptions(
            name='phongban',
            options={'verbose_name': 'Phòng Ban', 'verbose_name_plural': 'Phòng Ban'},
        ),
        migrations.AlterModelOptions(
            name='thannhan',
            options={'verbose_name': 'Thân Nhân', 'verbose_name_plural': 'Thân Nhân'},
        ),
        migrations.AlterModelOptions(
            name='trinhdongoaingu',
            options={'verbose_name': 'Trình Độ Ngoại Ngữ', 'verbose_name_plural': 'Trình Độ Ngoại Ngữ'},
        ),
        migrations.AddField(
            model_name='phieuluong',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
