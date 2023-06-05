# Generated by Django 4.2 on 2023-05-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainTitleName', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to='serverapp/static/blogImages')),
                ('video', models.FileField(blank=True, null=True, upload_to='serverapp/static/blogVideo')),
                ('summary', models.CharField(max_length=100)),
                ('subTitleNameFirst', models.CharField(blank=True, max_length=40, null=True)),
                ('paragarphFirst', models.CharField(blank=True, max_length=255, null=True)),
                ('subTitleNameSecond', models.CharField(blank=True, max_length=40, null=True)),
                ('paragarphSecond', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
