# Generated by Django 5.0.1 on 2024-01-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0005_recipe_shortinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="shortinfo",
            field=models.CharField(max_length=100),
        ),
    ]
