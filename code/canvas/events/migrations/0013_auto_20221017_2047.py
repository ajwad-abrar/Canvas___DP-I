# Generated by Django 3.0.5 on 2022-10-17 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_organization_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='event_id',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]