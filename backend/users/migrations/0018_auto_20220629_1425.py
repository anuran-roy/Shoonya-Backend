# Generated by Django 3.1.14 on 2022-06-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_auto_20220516_0657"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="new_email_verification_code",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name="user",
            name="old_email_update_code",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name="user",
            name="unverified_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
