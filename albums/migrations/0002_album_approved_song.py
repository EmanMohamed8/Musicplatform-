# Generated by Django 4.1.1 on 2023-01-07 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='approved',
            field=models.BooleanField(default=False, help_text=' Approve the album if its name is not explicit'),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(default='song_album__name', max_length=50)),
                ('song_image', models.ImageField(null=True, upload_to='images/%y/%m/%d')),
                ('song_audio', models.FileField(null=True, upload_to='music/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_album', to='albums.album')),
            ],
        ),
    ]
