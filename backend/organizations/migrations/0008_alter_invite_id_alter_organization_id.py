# Generated by Django 4.0.5 on 2022-06-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0007_auto_20220329_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
