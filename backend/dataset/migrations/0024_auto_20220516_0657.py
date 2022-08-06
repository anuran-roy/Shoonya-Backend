# Generated by Django 3.1.14 on 2022-05-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0023_auto_20220502_1329"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blocktext",
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
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                max_length=15,
                verbose_name="language",
            ),
        ),
        migrations.AlterField(
            model_name="ocrdocument",
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
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                max_length=15,
                verbose_name="language",
            ),
        ),
        migrations.AlterField(
            model_name="sentencetext",
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
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                max_length=15,
                verbose_name="language",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="input_language",
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
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                max_length=15,
                verbose_name="input_language",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="output_language",
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
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                max_length=15,
                verbose_name="output_language",
            ),
        ),
    ]
