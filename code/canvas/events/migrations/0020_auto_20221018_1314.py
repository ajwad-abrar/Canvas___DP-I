# Generated by Django 3.0.5 on 2022-10-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_merge_20221018_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
