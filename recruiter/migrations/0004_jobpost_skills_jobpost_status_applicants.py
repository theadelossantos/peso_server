# Generated by Django 4.2.5 on 2023-10-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0028_alter_allprofile_account'),
        ('recruiter', '0003_alter_jobpost_allprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=models.CharField(default='unset', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seekerFolder.allprofile')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.jobpost')),
            ],
        ),
    ]
