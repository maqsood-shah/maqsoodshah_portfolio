# Generated by Django 3.0.2 on 2020-01-29 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maqs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mails',
            name='name',
        ),
    ]