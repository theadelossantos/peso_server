# Generated by Django 4.2.5 on 2023-09-23 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0007_alter_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
