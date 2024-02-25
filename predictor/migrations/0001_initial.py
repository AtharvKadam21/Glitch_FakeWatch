# Generated by Django 3.2.4 on 2024-02-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='input_img.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='VideoPicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(default='input_video.mp4', upload_to='')),
            ],
        ),
    ]