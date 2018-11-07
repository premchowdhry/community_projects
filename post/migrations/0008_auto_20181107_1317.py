# Generated by Django 2.0.9 on 2018-11-07 13:17

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_merge_20181107_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=django_google_maps.fields.AddressField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('schools', 'Schools'), ('nature', 'Nature'), ('construction', 'Construction'), ('cleaning', 'Cleaning')], default='schools', max_length=12),
        ),
    ]
