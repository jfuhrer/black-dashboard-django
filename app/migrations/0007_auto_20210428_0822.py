# Generated by Django 2.2.10 on 2021-04-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210428_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisorysession',
            name='agenda',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='advisorysession',
            name='investment_details',
            field=models.TextField(blank=True),
        ),
    ]