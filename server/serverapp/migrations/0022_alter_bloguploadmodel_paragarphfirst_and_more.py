# Generated by Django 4.2 on 2023-06-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0021_alter_bloguploadmodel_paragarphfirst_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='paragarphFirst',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bloguploadmodel',
            name='paragarphSecond',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]