# Generated by Django 2.0.9 on 2018-11-07 00:41

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20181029_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=django_google_maps.fields.AddressField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=django_google_maps.fields.GeoLocationField(max_length=100),
        ),
    ]
