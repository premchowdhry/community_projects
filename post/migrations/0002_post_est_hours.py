# Generated by Django 2.1.2 on 2018-10-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='est_hours',
            field=models.IntegerField(default=1),
        ),
    ]
