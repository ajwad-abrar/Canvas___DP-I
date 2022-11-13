# Generated by Django 4.1.1 on 2022-11-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0024_rename_users_user"),
    ]

    operations = [
        migrations.DeleteModel(name="Organization",),
        migrations.AddField(
            model_name="user", name="isAdmin", field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="isOrganization",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user", name="isUser", field=models.BooleanField(default=True),
        ),
    ]