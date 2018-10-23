# Generated by Django 2.0.9 on 2018-10-22 19:11

from django.db import migrations, models
import django.utils.timezone
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_est_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='est_hours',
            new_name='estimate_hours',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.get_image_path),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='work_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
