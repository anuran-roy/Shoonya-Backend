# Generated by Django 3.1.14 on 2022-05-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0021_auto_20220502_1329"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("MonolingualTranslation", "MonolingualTranslation"),
                    ("TranslationEditing", "TranslationEditing"),
                    ("ContextualTranslationEditing", "ContextualTranslationEditing"),
                    ("OCRAnnotation", "OCRAnnotation"),
                    ("MonolingualCollection", "MonolingualCollection"),
                    ("SentenceSplitting", "SentenceSplitting"),
                    (
                        "ContextualSentenceVerification",
                        "ContextualSentenceVerification",
                    ),
                ],
                help_text="Project Type indicating the annotation task",
                max_length=100,
            ),
        ),
    ]
