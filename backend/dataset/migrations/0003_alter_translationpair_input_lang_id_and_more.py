# Generated by Django 4.0.1 on 2022-03-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0002_alter_sentencetext_lang_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translationpair",
            name="input_lang_id",
            field=models.CharField(
                choices=[
                    ("bn", "Bengali"),
                    ("gu", "Gujarati"),
                    ("en", "English"),
                    ("hi", "Hindi"),
                    ("kn", "Kannada"),
                    ("mr", "Marathi"),
                    ("ne", "Nepali"),
                    ("ne", "Odia"),
                    ("pa", "Punjabi"),
                    ("sa", "Sanskrit"),
                    ("ta", "Tamil"),
                    ("te", "Telugu"),
                ],
                max_length=3,
                verbose_name="input_language_id",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="output_lang_id",
            field=models.CharField(
                choices=[
                    ("bn", "Bengali"),
                    ("gu", "Gujarati"),
                    ("en", "English"),
                    ("hi", "Hindi"),
                    ("kn", "Kannada"),
                    ("mr", "Marathi"),
                    ("ne", "Nepali"),
                    ("ne", "Odia"),
                    ("pa", "Punjabi"),
                    ("sa", "Sanskrit"),
                    ("ta", "Tamil"),
                    ("te", "Telugu"),
                ],
                max_length=3,
                verbose_name="output_language_id",
            ),
        ),
    ]
