# Generated by Django 5.0.6 on 2024-05-31 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eventapp", "0004_alter_attendee_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendee",
            name="location",
            field=models.TextField(blank=True, null=True),
        ),
    ]