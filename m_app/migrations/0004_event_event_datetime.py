# Generated by Django 5.0 on 2023-12-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0003_location_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]