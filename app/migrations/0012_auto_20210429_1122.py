# Generated by Django 2.2.10 on 2021-04-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210429_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='reminder_date',
        ),
        migrations.AddField(
            model_name='notes',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Zu erledigen bis'),
        ),
    ]
