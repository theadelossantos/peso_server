# Generated by Django 4.2.5 on 2023-10-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0031_alter_allprofile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster_profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
