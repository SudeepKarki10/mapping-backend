# Generated by Django 5.0 on 2023-12-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0014_remove_event_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_datetime',
            field=models.DateField(null=True),
        ),
    ]