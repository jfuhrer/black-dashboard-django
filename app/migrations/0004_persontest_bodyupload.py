# Generated by Django 2.2.10 on 2021-04-27 07:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_persontest_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontest',
            name='bodyUpload',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
