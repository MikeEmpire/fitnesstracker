# Generated by Django 4.2.19 on 2025-03-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutplan',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
