# Generated by Django 4.1.1 on 2023-08-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_options_remove_artist_stagename'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
