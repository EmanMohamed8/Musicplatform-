# Generated by Django 4.1.1 on 2023-07-25 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='dateTime',
            new_name='release_datetime',
        ),
    ]
