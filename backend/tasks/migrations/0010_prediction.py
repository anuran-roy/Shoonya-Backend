# Generated by Django 3.1.14 on 2022-03-28 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0009_auto_20220323_1429"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prediction",
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
                (
                    "result",
                    models.JSONField(
                        default=dict,
                        help_text="Prediction result",
                        null=True,
                        verbose_name="result",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="predictions",
                        to="tasks.task",
                        verbose_name="prediction_task_id",
                    ),
                ),
            ],
        ),
    ]
