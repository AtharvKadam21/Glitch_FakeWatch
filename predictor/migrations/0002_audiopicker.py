# Generated by Django 3.2.4 on 2024-02-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioPicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(default='input_audio.mp3', upload_to='')),
            ],
        ),
    ]
