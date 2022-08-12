# Generated by Django 3.1.14 on 2022-04-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_remove_user_maximum_annotations_per_day"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="lang_id",
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[
                    ("English", "English"),
                    ("Assamese", "Assamese"),
                    ("Bengali", "Bengali"),
                    ("Bodo", "Bodo"),
                    ("Dogri", "Dogri"),
                    ("Gujarati", "Gujarati"),
                    ("Hindi", "Hindi"),
                    ("Kannada", "Kannada"),
                    ("Kashmiri", "Kashmiri"),
                    ("Konkani", "Konkani"),
                    ("Maithili", "Maithili"),
                    ("Malayalam", "Malayalam"),
                    ("Manipuri", "Manipuri"),
                    ("Marathi", "Marathi"),
                    ("Nepali", "Nepali"),
                    ("Odia", "Odia"),
                    ("Punjabi", "Punjabi"),
                    ("Sanskrit", "Sanskrit"),
                    ("Santali", "Santali"),
                    ("Sindhi", "Sindhi"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                default="English",
                max_length=15,
                verbose_name="language",
            ),
        ),
    ]
