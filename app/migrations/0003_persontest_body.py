# Generated by Django 2.2.10 on 2021-04-27 06:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_advisorysession_advisorysessionsummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontest',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
