# Generated by Django 3.1.14 on 2022-07-01 09:34

from django.db import migrations, models
import django.utils.timezone


def set_my_defaults(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    for project in Project.objects.all().iterator():
        project.created_at = project.organization_id.created_at
        project.save()


def reverse_func(apps, schema_editor):
    pass  # code for reverting migration, if any


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0026_alter_project_src_language_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="Project Created At",
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_my_defaults, reverse_func),
    ]
