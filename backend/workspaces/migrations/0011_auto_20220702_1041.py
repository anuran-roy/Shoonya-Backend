# Generated by Django 3.1.14 on 2022-07-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0010_alter_workspace_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
