# Generated by Django 5.0.1 on 2024-01-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0003_alter_recipe_steps"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.TextField(),
        ),
    ]
