# Generated by Django 2.2.10 on 2021-04-29 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_notes_reminder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='body',
            new_name='text',
        ),
    ]
