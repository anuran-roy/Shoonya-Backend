# Generated by Django 3.1.14 on 2022-06-16 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0024_project_frozen_users_alter_project_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="max_pending_tasks_per_user",
            field=models.IntegerField(
                default=60,
                help_text="Maximum no. of tasks assigned to a user which are at unlabeled stage, as a threshold for pulling new tasks",
                verbose_name="max_pending_tasks_per_user",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="tasks_pull_count_per_batch",
            field=models.IntegerField(
                default=10,
                help_text="Maximum no. of new tasks that can be assigned to a user at once",
                verbose_name="tasks_pull_count_per_batch",
            ),
        ),
        migrations.CreateModel(
            name="ProjectTaskRequestLock",
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
                ("expires_at", models.DateTimeField(verbose_name="expires_at")),
                (
                    "project",
                    models.ForeignKey(
                        help_text="Project locked for task pulling",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lock",
                        to="projects.project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User locking this project to pull tasks",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_lock",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
