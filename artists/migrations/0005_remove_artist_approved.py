# Generated by Django 4.1.1 on 2023-08-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_artist_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='approved',
        ),
    ]
