# Generated by Django 3.2 on 2022-08-26 21:07

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_supremeuser_bio_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supremeuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/profile.jpg', null=True, upload_to=Users.models.profilepicture_upload_path),
        ),
    ]