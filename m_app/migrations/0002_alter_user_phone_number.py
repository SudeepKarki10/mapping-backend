# Generated by Django 5.0 on 2023-12-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]