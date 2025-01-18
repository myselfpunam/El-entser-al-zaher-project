# Generated by Django 5.1.5 on 2025-01-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaher_app', '0003_contactinfo_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='closing_day',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='open_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='opening_day',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
