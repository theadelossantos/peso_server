# Generated by Django 4.2.5 on 2023-10-14 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0028_alter_allprofile_account'),
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='profile',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='allprofile',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, to='seekerFolder.allprofile'),
            preserve_default=False,
        ),
    ]