# Generated by Django 3.0.8 on 2020-09-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200914_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts/', verbose_name='Изображения'),
        ),
    ]
