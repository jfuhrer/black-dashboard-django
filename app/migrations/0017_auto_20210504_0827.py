# Generated by Django 2.2.10 on 2021-05-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210504_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='evt_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am'),
        ),
    ]