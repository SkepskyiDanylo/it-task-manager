# Generated by Django 5.1.4 on 2025-01-11 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0013_task_completed_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects",
                to="manager.team",
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="workers",
                to="manager.position",
            ),
        ),
    ]