# Generated by Django 3.1.14 on 2022-04-04 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0015_auto_20220401_0700"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskLock",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("expire_at", models.DateTimeField(verbose_name="expire_at")),
                (
                    "task",
                    models.ForeignKey(
                        help_text="Locked task",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="locks",
                        to="tasks.task",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User who locked this task",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_locks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
