# Generated by Django 5.0.6 on 2024-05-21 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eventapp", "0002_registration"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendee",
            name="check_in_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="attendee",
            name="event",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eventapp.event",
            ),
        ),
        migrations.AlterField(
            model_name="attendee",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
