# Generated by Django 3.0.3 on 2020-09-14 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200914_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='publish_date',
            field=models.TextField(blank=True, verbose_name='Thời gian đăng'),
        ),
        migrations.AlterField(
            model_name='item',
            name='send_date',
            field=models.TextField(blank=True, verbose_name='Thời gian gửi'),
        ),
    ]