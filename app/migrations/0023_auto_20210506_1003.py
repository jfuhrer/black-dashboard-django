# Generated by Django 2.2.10 on 2021-05-06 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210506_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankEmployees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Vorname')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Nachname')),
                ('role', models.CharField(blank=True, choices=[('advisor_m', 'Kundenbetreuer'), ('advisor_f', 'Kundenbetreuerin'), ('bachoffice', 'Back-Office'), ('manager', 'Manager')], max_length=150, verbose_name='Rolle')),
                ('email', models.CharField(blank=True, max_length=150, verbose_name='E-Mail')),
                ('telephone_no', models.CharField(blank=True, max_length=150, verbose_name='Telefon')),
            ],
        ),
        migrations.AlterField(
            model_name='advisorysession',
            name='date',
            field=models.DateTimeField(verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='advisorysession',
            name='evt_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am'),
        ),
        migrations.AlterField(
            model_name='advisorysession',
            name='evt_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Verändert am'),
        ),
        migrations.AlterField(
            model_name='advisorysession',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='advisorysession',
            name='type',
            field=models.CharField(choices=[('advisory', 'Beratung'), ('next-advisory', 'Bevorstehende Beratung'), ('event', 'Event')], max_length=150),
        ),
        migrations.AddField(
            model_name='advisorysession',
            name='advisor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.BankEmployees'),
        ),
    ]
