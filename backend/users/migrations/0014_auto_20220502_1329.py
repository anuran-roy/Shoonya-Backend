# Generated by Django 3.1.14 on 2022-05-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_auto_20220429_0542"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activity_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="last annotation activity by the user"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="availability_status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Available"), (2, "On Leave")],
                default=1,
                help_text="Indicates whether a user is available for doing annotation or not.",
            ),
        ),
    ]
