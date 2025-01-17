# Generated by Django 3.1.14 on 2022-06-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0024_auto_20220518_0847"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="task_status",
            field=models.CharField(
                choices=[
                    ("unlabeled", "unlabeled"),
                    ("labeled", "labeled"),
                    ("skipped", "skipped"),
                    ("accepted", "accepted"),
                    ("freezed", "freezed"),
                    ("rejected", "rejected"),
                    ("draft", "draft"),
                ],
                default="unlabeled",
                max_length=100,
                verbose_name="task_status",
            ),
        ),
    ]
