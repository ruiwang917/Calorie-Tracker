# Generated by Django 5.0.6 on 2024-06-20 08:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_consume"),
    ]

    operations = [
        migrations.RenameField(
            model_name="food",
            old_name="fat",
            new_name="fats",
        ),
    ]
