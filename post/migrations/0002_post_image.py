# Generated by Django 4.0.4 on 2022-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='post_img'),
            preserve_default=False,
        ),
    ]
