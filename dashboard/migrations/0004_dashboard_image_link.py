# Generated by Django 2.0.9 on 2018-11-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20181112_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='image_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
