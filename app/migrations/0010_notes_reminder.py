# Generated by Django 2.2.10 on 2021-04-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_notes_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='reminder',
            field=models.BooleanField(default=False),
        ),
    ]