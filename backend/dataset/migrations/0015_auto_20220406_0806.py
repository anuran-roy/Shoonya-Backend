# Generated by Django 3.1.14 on 2022-04-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0014_auto_20220329_0911"),
    ]

    operations = [
        migrations.AddField(
            model_name="ocrdocument",
            name="image_url",
            field=models.URLField(
                default="", max_length=500, verbose_name="bucket_url_for_image"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ocrdocument",
            name="page_number",
            field=models.IntegerField(default=1, verbose_name="page_number"),
        ),
        migrations.AlterField(
            model_name="ocrdocument",
            name="file_url",
            field=models.URLField(
                blank=True,
                max_length=500,
                null=True,
                verbose_name="bucket_url_for_file",
            ),
        ),
    ]
