# Generated by Django 4.0.6 on 2022-08-16 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='media_name',
        ),
    ]
