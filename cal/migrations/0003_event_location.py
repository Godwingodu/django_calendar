# Generated by Django 3.2.12 on 2023-03-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_rename_title_event_programme_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='null', max_length=50),
        ),
    ]