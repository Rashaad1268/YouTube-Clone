# Generated by Django 3.1.7 on 2021-03-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_video_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorprofile',
            name='profile_picture',
            field=models.ImageField(default='static/pictures/profile_pic.jpg', upload_to='images/profile_pics'),
        ),
    ]