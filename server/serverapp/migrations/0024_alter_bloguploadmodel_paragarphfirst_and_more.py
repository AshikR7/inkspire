# Generated by Django 4.2 on 2023-06-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0023_alter_bloguploadmodel_maintitlename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='paragarphFirst',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='paragarphSecond',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
