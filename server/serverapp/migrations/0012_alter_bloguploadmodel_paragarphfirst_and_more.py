# Generated by Django 4.2 on 2023-05-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0011_alter_bloguploadmodel_paragarphsecond_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='paragarphFirst',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='paragarphSecond',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='subTitleNameSecond',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]