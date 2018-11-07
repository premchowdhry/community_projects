# Generated by Django 2.0.9 on 2018-11-07 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(choices=[('schools', 'Schools'), ('nature', 'Nature'), ('construction', 'Construction'), ('cleaning', 'Cleaning')], default='schools', max_length=12)),
                ('estimate_hours', models.IntegerField(default=1)),
                ('work_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('description', models.TextField(default='')),
                ('company', models.CharField(default='', max_length=100)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to=post.models.get_image_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
