# Generated by Django 4.2.4 on 2023-08-06 11:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_done", "created"]},
        ),
    ]
