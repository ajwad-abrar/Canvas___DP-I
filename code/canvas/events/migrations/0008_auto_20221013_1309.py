# Generated by Django 3.0.5 on 2022-10-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20221013_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='profile_picture',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
