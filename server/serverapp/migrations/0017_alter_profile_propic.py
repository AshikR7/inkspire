# Generated by Django 4.2 on 2023-06-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0016_alter_profile_propic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='proPic',
            field=models.ImageField(blank=True, upload_to='serverapp/static/profile_pictures/'),
        ),
    ]
