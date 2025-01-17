# Generated by Django 3.1.14 on 2022-03-20 07:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("workspaces", "0003_auto_20220320_0635"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workspace",
            name="manager",
            field=models.ManyToManyField(
                related_name="workspace_manager",
                to=settings.AUTH_USER_MODEL,
                verbose_name="manager",
            ),
        ),
    ]
