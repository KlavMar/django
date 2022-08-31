# Generated by Django 4.0.6 on 2022-08-16 14:35

import contextlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_media_media_remove_post_image_media_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='media',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, null=contextlib.nullcontext, upload_to=''),
        ),
    ]
