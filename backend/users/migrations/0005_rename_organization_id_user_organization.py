# Generated by Django 3.2.12 on 2022-02-14 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_user_invite_accepted"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="organization_id",
            new_name="organization",
        ),
    ]
