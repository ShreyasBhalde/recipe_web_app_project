# Generated by Django 5.0.1 on 2024-01-08 09:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0011_recipe_addedby"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="uploading_date",
        ),
    ]
