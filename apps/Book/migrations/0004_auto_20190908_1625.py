# Generated by Django 2.2.5 on 2019-09-08 08:25

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20190907_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookDesc',
            field=tinymce.models.HTMLField(verbose_name='图书简介'),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookFile',
            field=models.FileField(max_length='100', upload_to='file', verbose_name='图书文件'),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookPhoto',
            field=models.ImageField(max_length='80', upload_to='img', verbose_name='图书图片'),
        ),
    ]
