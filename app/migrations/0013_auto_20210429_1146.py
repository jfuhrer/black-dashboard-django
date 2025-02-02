# Generated by Django 2.2.10 on 2021-04-29 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210429_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='advisory_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.AdvisorySession'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Zu erledigen bis'),
        ),
    ]
