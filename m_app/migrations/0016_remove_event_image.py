# Generated by Django 5.0 on 2023-12-23 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0015_alter_event_event_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]